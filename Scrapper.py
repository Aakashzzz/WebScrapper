import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Website Connected Successfully!")
else:
    print("Connection Failed")

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_names = []
prices = []

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip().replace("Â", "")

    book_names.append(name)
    prices.append(price)

data = pd.DataFrame({
    "Book Name": book_names,
    "Price": prices
})

print(data)

data.to_csv("books.csv", index=False)

print("\nCSV File Saved Successfully!")