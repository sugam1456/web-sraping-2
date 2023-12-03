import requests
from bs4 import BeautifulSoup
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
headers = ["Name", "Distance", "Mass", "Radius"]
star_data = []
response = requests.get(START_URL)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    target_table = tables[0]
    rows = target_table.find_all('tr')
    for row in rows[1:]:  
        columns = row.find_all('td')
        star_info = [column.get_text(strip=True) for column in columns]
        star_data.append(star_info)
    print(star_data[0])
else:
    print(f"Unable to connect to page. Status code: {response.status_code}")
