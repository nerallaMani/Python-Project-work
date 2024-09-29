from bs4 import BeautifulSoup as bs
import requests
import re

# Step 1: Web Scraping Product Data from Meesho
url = 'https://www.meesho.com/tshirts-men/pl/3k8'
response = requests.get(url)

# Parse the HTML content
soup = bs(response.content, 'html.parser')

# Extract product titles and prices (top 20)
titles = soup.find_all('p', class_="NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5")[:20]
prices = soup.find_all('h5', class_='sc-eDvSVe dwCrSh')[:20]

# Step 2: Store Product Data in a Text File
try:
    with open('product_data.txt', 'w', encoding='utf-8') as fp:
        for title, price in zip(titles, prices):
            fp.write(f'Title: {title.text.strip()} | Price: {price.text.strip()}\n')
except FileExistsError:
    print('File already exists! Please change the filename if needed.')

# Step 3: Read and Extract Data Using Regex
try:
    with open('product_data.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        product_titles = re.findall(r"Title: (.*?) \| Price:", data)
        product_prices = re.findall(r'\d+', data)

        # Display Product Names and Prices
        print('-' * 100)
        print(f"\t Product Name \t\t\t\t\t\t Price")
        print('-' * 100)
        for name, price in zip(product_titles, product_prices):
            print(f'{name.strip()} \t\t\t\t {price}')
        print('-' * 100)

except FileNotFoundError:
    print("The file does not exist, please check and try again!")
