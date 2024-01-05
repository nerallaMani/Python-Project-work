import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def get_stock_data(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad requests
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        return None
    except requests.exceptions.RequestException as err:
        print ("Request Error:",err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    stock_price_element = soup.find('span', {'data-reactid': '50'})
    volume_element = soup.find('td', {'data-test': 'OPEN-value'})
    market_cap_element = soup.find('td', {'data-test': 'MARKET_CAP-value'})

    # Extract only numeric values from HTML elements
    stock_price = stock_price_element.text.strip() if stock_price_element else None
    volume = volume_element.text.strip() if volume_element else None
    market_cap = market_cap_element.text.strip() if market_cap_element else None

    # Create a Pandas DataFrame
    data = {
        'Symbol': [symbol],
        'Stock Price': [stock_price],
        'Volume': [volume],
        'Market Cap': [market_cap],
        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    }

    df = pd.DataFrame(data)
    return df

def main():
    # Replace 'AAPL' with the desired stock symbol
    symbol = 'AAPL'

    while True:
        stock_data = get_stock_data(symbol)

        if stock_data is not None:
            # Append data to a CSV file or your preferred storage method
            with open('stock_data.csv', 'a') as f:
                stock_data.to_csv(f, header=f.tell() == 0, index=False)

        # Run the script every hour (3600 seconds)
        time.sleep(3600)

if __name__ == '__main__':
    main()
