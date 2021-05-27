import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doMfd=yes&type=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = table = soup.find_all("table")

df = pd.read_html(str(table))[0]

df1 = df.iloc[:-1,:-1]
print(df1)