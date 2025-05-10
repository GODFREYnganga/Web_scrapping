from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_Australian_companies'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)
soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')
print(table)

Aust_Companies_titles = table.find_all('th')
print(Aust_Companies_titles)
Aust_table_Companies_titles = [title.text.strip() for title in Aust_Companies_titles]
print(Aust_table_Companies_titles)

import pandas as pd
df = pd.DataFrame(columns=Aust_table_Companies_titles)
df

Column_data = table.find_all('tr')
for row in Column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data
df

df.to_csv(r'C:\Users\Admin\Desktop\Self_learn\Australia_companies.csv', index=False)
