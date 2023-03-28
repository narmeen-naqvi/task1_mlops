'''
A02
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.worldometers.info/coronavirus/'
response = requests.get(URL, timeout=10)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', id='main_table_countries_today')

data = []

# Extract table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())
data.append(headers)

# Extract table rows
for tr in table.tbody.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    # Filter out rows that are not country rows
    if row and row[0].isalpha():
        data.append(row)

# Create a pandas dataframe from the data
df = pd.DataFrame(data[1:], columns=data[0])

# Print the dataframe
print(df.head())

