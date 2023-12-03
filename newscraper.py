import requests
from bs4 import BeautifulSoup
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Brown_dwarf"
response = requests.get(START_URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    target_table = tables[2]
    rows = []
    table_rows = target_table.find_all('tr')
    for row in table_rows[1:]: 
        columns = row.find_all('td')
        row_data = [column.get_text(strip=True) for column in columns]
        rows.append(row_data)
    star_data = []

    for row in rows:
        if len(row) >= 4:
            star_name = row[0]
            radius = row[1]
            mass = row[2]
            distance = row[3]
            star_data.append([star_name, radius, mass, distance])

    columns = ["Star Name", "Radius", "Mass", "Distance"]
    df = pd.DataFrame(star_data, columns=columns)

    df.to_csv('dwarf_stars.csv', index=False, encoding='utf-8')

    print("Data has been successfully scraped and saved to 'dwarf_stars.csv'.")

else:
    print(f"Unable to connect the page. Status code: {response.status_code}")
