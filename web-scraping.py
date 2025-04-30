import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import uniform
import os

# Configure headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

def scrape_imdb_top250():
    url = 'https://www.imdb.com/chart/top/'
    
    try:
        print("Fetching IMDB Top 250 page...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        if "Top 250 Movies" not in response.text:
            print("Didn't get the expected content. IMDB might be blocking us.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    movies_data = []
    
    # Updated selectors for current IMDB structure
    movie_rows = soup.select('ul.ipc-metadata-list > li.ipc-metadata-list-summary-item')
    
    if not movie_rows:
        print("No movies found - page structure may have changed")
        return None
    
    print(f"Found {len(movie_rows)} movies to process...")
    
    for rank, row in enumerate(movie_rows[:250], 1):  # Limit to 250
        sleep(uniform(1, 2))  # Respectful delay
        
        try:
            # Title and URL
            title_element = row.select_one('h3.ipc-title__text')
            if not title_element:
                continue
                
            title = title_element.get_text(strip=True).split('. ')[-1]
            movie_url = 'https://www.imdb.com' + row.select_one('a.ipc-title-link-wrapper')['href'].split('?')[0]
            
            # Year
            year_element = row.select_one('span.cli-title-metadata-item')
            year = year_element.get_text(strip=True) if year_element else "N/A"
            
            # Rating
            rating_element = row.select_one('span.ipc-rating-star--imdb')
            rating = rating_element.get_text(strip=True).split()[0] if rating_element else "N/A"
            
            # Votes (from aria-label)
            votes = "N/A"
            if rating_element and 'aria-label' in rating_element.attrs:
                votes_text = rating_element['aria-label']
                votes_parts = votes_text.split()
                if len(votes_parts) >= 4:
                    votes = votes_parts[3].replace(',', '')
            
            movies_data.append({
                'Rank': rank,
                'Title': title,
                'Year': year,
                'Rating': rating,
                'Votes': votes,
                'URL': movie_url
            })
            
            if rank % 25 == 0:
                print(f"Processed {rank} movies...")
                
        except Exception as e:
            print(f"Error processing movie {rank}: {str(e)[:100]}...")
            continue
    
    return pd.DataFrame(movies_data)

# Run the scraper
print("Starting IMDB Top 250 scraping...")
imdb_df = scrape_imdb_top250()

if imdb_df is not None and not imdb_df.empty:
    print("\nScraping completed successfully!")
    print(f"Total movies scraped: {len(imdb_df)}")
    print("\nSample data:")
    print(imdb_df.head())
    
    # Save to CSV with proper file handling
    save_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'imdb_top250.csv')
    try:
        imdb_df.to_csv(save_path, index=False)
        print(f"\nData saved to: {save_path}")
    except PermissionError:
        print("\nCould not save file - permission denied. Trying alternative location...")
        try:
            save_path = 'imdb_top250_output.csv'
            imdb_df.to_csv(save_path, index=False)
            print(f"Data saved to: {save_path}")
        except Exception as e:
            print(f"Failed to save file: {e}")
else:
    print("Scraping failed. No data was collected.")

#keep window open & closes only if user press enter button
input("\nPress Enter to exit...")