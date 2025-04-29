#this code is working perfectly
#but, you cannot scrape the data as imdb is blocking
#use "web-scraping.py" to scrape the data properly from IMBD.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
from random import uniform

# Set headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_imdb_top250():
    url = 'https://www.imdb.com/chart/top/'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching main page: {e}")
        return None

    soup = BeautifulSoup(response.content, 'lxml')
    
    # Initialize lists to store data
    data = {
        'rank': [],
        'title': [],
        'year': [],
        'rating': [],
        'votes': [],
        'crew': [],
        'movie_url': []
    }
    
    # Find all movie rows in the chart
    movie_rows = soup.select('tbody.lister-list tr')
    
    for row in movie_rows:
        # Add delay to avoid being blocked
        sleep(uniform(0.5, 1.5))
        
        # Rank
        rank = row.find('td', class_='posterColumn').get_text(strip=True).split('.')[0]
        data['rank'].append(rank)
        
        # Title and URL
        title_column = row.find('td', class_='titleColumn')
        title = title_column.find('a').get_text(strip=True)
        data['title'].append(title)
        
        # Year
        year = title_column.find('span').get_text(strip=True).strip('()')
        data['year'].append(year)
        
        # Rating
        rating = row.find('td', class_='ratingColumn imdbRating').strong.get_text(strip=True)
        data['rating'].append(rating)
        
        # Crew (director and actors)
        crew = title_column.find('a')['title']
        data['crew'].append(crew)
        
        # Votes (from title attribute)
        rating_element = row.find('td', class_='ratingColumn imdbRating')
        votes = rating_element.strong['title'].split()[-2].replace(',', '')
        data['votes'].append(votes)
        
        # Movie URL
        movie_path = title_column.find('a')['href']
        movie_url = f"https://www.imdb.com{movie_path}"
        data['movie_url'].append(movie_url)
    
    return pd.DataFrame(data)

# Run the scraper
imdb_df = scrape_imdb_top250()

if imdb_df is not None:
    print(f"Successfully scraped {len(imdb_df)} movies")
    print(imdb_df.head())
    
    # Save to CSV
    imdb_df.to_csv('imdb_top250.csv', index=False)
    print("Data saved to 'imdb_top250.csv'")
else:
    print("Scraping failed")