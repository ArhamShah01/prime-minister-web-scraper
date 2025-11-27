import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="wikitable")
print("Found", len(tables), "tables")

prime_ministers = []

for table in tables:
    rows = table.find_all("tr")
    if len(rows) < 2:
        continue

    # pick the table whose first data row has a portrait image
    first_data_row = rows[1]
    if not first_data_row.find("img"):
        continue

    # in this table, every PM row has the name in a <b> tag
    for row in rows[1:]:
        bold = row.find("b")
        if not bold:
            continue
        name = bold.get_text(strip=True)
        name = name.replace("†", "").replace("§", "").strip()
        if name:
            prime_ministers.append(name)
    break

print("\nPrime Ministers of India:")
print("-" * 30)
for i, pm in enumerate(prime_ministers, 1):
    print(f"{i}. {pm}")
print("\nTotal:", len(prime_ministers), "Prime Ministers")
