# Web Scraper: List of Prime Ministers of India

## Description

This is a simple Python web-scraping script that fetches the Wikipedia page “List of prime ministers of India” and extracts the names of all prime ministers using the BeautifulSoup library.[web:2] The script parses the main wikitable on the page, locates the bold text in each data row (which corresponds to the prime minister’s name), and prints the names in order.[attached_file:1][web:2]

## Features

- Sends an HTTP GET request to the Wikipedia article for Indian prime ministers.[web:2]
- Parses HTML with BeautifulSoup and locates the relevant wikitable.
- Automatically identifies the correct table by checking for a portrait image in the first data row.[attached_file:1][web:2]
- Extracts and cleans prime-minister names from bold tags in the name column.
- Prints a numbered list of all prime ministers and the total count.

## Requirements

- Python 3.x
- Packages:
  - `requests`
  - `beautifulsoup4`

Install dependencies:
pip install requests beautifulsoup4


## Usage

1. Clone or download this repository.
2. Install the required packages.
3. Run the script: python web-scraping.py
4. The script will:
   - Request the HTML of the Wikipedia page.
   - Parse the page and find all tables with class `wikitable`.
   - Select the table whose first data row contains a portrait image.
   - Iterate through each row, find the bolded name, and append it to a list.
   - Print the ordered list of prime ministers and the total number found.[attached_file:1][web:2]

## How it works

- A custom `User-Agent` header is sent so that Wikipedia returns the full desktop HTML page.[web:18]
- BeautifulSoup builds a parse tree from the HTML response.
- A simple heuristic (portrait image in the first cell) is used to detect the prime-minister table.
- Each table row is scanned for a `<b>` tag; the text inside is treated as the prime minister’s name.
- Symbols like `†` and `§` are stripped before printing.[attached_file:1][web:2]

## Notes

- This project is for learning and demonstration purposes and respects Wikipedia’s terms of use and intellectual property; it only extracts publicly visible factual data (names) without reproducing any proprietary text.[web:2][web:7]
- If Wikipedia’s HTML structure changes, the selector logic (table detection or bold-tag search) may need adjustments.


