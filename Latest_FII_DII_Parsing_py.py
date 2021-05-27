import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.fpi.nsdl.co.in/web/Reports/Latest.aspx'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find("table",{"class":"tbls01"})

df = pd.read_html(str(table))[0]
df1 =df.iloc[:-1,:]
print(df1)