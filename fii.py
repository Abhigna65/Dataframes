from bs4 import BeautifulSoup
import requests
import pandas as pd


#url = 'https://www1.nseindia.com/products/dynaContent/equities/equities/htms/fiiEQ.htm'
url = 'https://www1.nseindia.com/products/dynaContent/equities/equities/htms/fiiEQ.htm'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(url, headers=headers).text


soup = BeautifulSoup(response, 'lxml')
tables = soup.find_all('table', class_='holiday_list')
for table in tables:
    table_rows = table.find_all('tr')
    tablerows = []
    for table_row in table_rows:
        table_headers = table_row.find_all('th')
        tableheader = []
        for table_header in table_headers:
            tableheader.append(table_header.text)
        tablerows.append(tableheader)
        table_data = table_row.find_all('td')
        tabledata = []
        for table_data_row in table_data:
            tabledata.append(table_data_row.text)
        tablerows.append(tabledata)
       

tablerows =  [x for x in tablerows if x]
#columns = tablerows[1]
#df = pd.DataFrame(tablerows[1:])
#df.reset_index(drop=True, inplace=True)
#print(df)
data  = {}
for col in range(len(tablerows[1])):
    data[tablerows[1][col]] = [tablerows[2][col]]

print(data)
df = pd.DataFrame(data)
print(df)
print(df.columns)