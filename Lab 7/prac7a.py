import requests
from bs4 import BeautifulSoup

url = "https://finviz.com"

# Send a GET request to the website
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "stock-table"})
rows = table.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    if len(cells) > 0:
        stock_name = cells[0].text
        stock_price = cells[1].text
        print(f"{stock_name}: {stock_price}")
