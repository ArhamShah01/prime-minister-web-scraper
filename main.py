import requests
from bs4 import BeautifulSoup

# Wikipedia URL for Indian Prime Ministers
url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India"

# Headers to mimic a browser request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

# Fetch the webpage and parse HTML
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all wiki tables on the page
tables = soup.find_all("table", class_="wikitable")
print("Found", len(tables), "tables")

prime_ministers = []

# Iterate through tables to find the one with PM data
for table in tables:
    rows = table.find_all("tr")
    if len(rows) < 2:
        continue

    # Pick the table whose first data row has a portrait image
    first_data_row = rows[1]
    if not first_data_row.find("img"):
        continue

    # Extract PM names from bold tags in this table
    for row in rows[1:]:
        bold = row.find("b")
        if not bold:
            continue
        
        # Clean up the name by removing special characters
        name = bold.get_text(strip=True)
        name = name.replace("†", "").replace("§", "").strip()
        
        if name:
            prime_ministers.append(name)
    break

# Display results
print("\nPrime Ministers of India:")
print("-" * 30)
for i, pm in enumerate(prime_ministers, 1):
    print(f"{i}. {pm}")
print("\nTotal:", len(prime_ministers), "Prime Ministers")
