import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def extract_product_data(soup):
    products = []
    articles = soup.find_all('article', class_='product_pod')
    for article in articles:
        name = article.h3.a['title']
        price = article.find('p', class_='price_color').text.strip().replace('£', '')
        rating_class = article.p['class'][1]  # e.g., 'Three'
        rating = rating_class
        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })
    return products

def main():
    all_products = []
    for page in range(1, 3):  # Scrape first 2 pages for demonstration
        print(f"Scraping page {page}...")
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        products = extract_product_data(soup)
        all_products.extend(products)

    # Save to CSV
    df = pd.DataFrame(all_products)
    df.to_csv('products.csv', index=False)
    print("Data saved to products.csv")

if __name__ == "__main__":
    main()
