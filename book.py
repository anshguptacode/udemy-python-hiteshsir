import requests
from bs4 import BeautifulSoup
import csv

def scrape_books(url):
    """
    Scrapes book titles and prices from books.toscrape.com and saves to a CSV file.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    scraped_data = []
    print(f"Found {len(books)} books on the page.")

    for book in books:
        title_element = book.find('h3').find('a')
        title = title_element['title'] if title_element else 'No Title'
        price_element = book.find('p', class_='price_color')
        price = price_element.get_text() if price_element else 'No Price'
        scraped_data.append({'title': title, 'price': price})

    try:
        with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(scraped_data)
        print("Data successfully saved to books.csv")
    except IOError as e:
        print(f"Error writing to file: {e}")
        
    return scraped_data

if __name__ == '__main__':
    target_url = 'http://books.toscrape.com/'
    data = scrape_books(target_url)
