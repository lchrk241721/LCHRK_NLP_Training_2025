import re
import requests

please_wait = "===Extracting Ebook Data Is In Progress. Please Wait A While!...==="
print(please_wait)
def get_book(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        raw = response.text
        
        # Find start marker (more flexible pattern)
        start_match = re.search(r"\*\*\* START OF (THIS|THE) PROJECT GUTENBERG EBOOK .*? \*\*\*", raw)
        if not start_match:
            raise ValueError("Could not find start marker in the text")
        start = start_match.end()
        
        # Find end marker
        end_match = re.search(r"\*\*\* END OF (THIS|THE) PROJECT Gutenberg EBOOK .*? \*\*\*", raw, re.IGNORECASE)
        if not end_match:
            raise ValueError("Could not find end marker in the text")
        end = end_match.start()
        
        return raw[start:end]
    
    except Exception as e:
        print(f"Error processing book: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice
    book_text = get_book(url)
    if book_text:
        print(book_text[:1000])  # Print first 1000 characters

#Perform some exploratory data analysis on this data using regex
#Count number of times "the" is appeared in the book

exp_da = len(re.findall(r'the', book_text))
exp_data_analysis = "===Exploratory Data Analysis==="
print(exp_data_analysis)
print(exp_da)

#find all occurance of text in the format "abc--xyz"
foc = re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book_text)
foct = "===Find Occurences==="
print(foct)
print(foc)

#keep window open & closes only if user press enter button
input("\nPress Enter to exit...")