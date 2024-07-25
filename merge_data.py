import pandas as pd
from bs4 import BeautifulSoup
import os
import glob

directory = 'data/raw/'

html_files = glob.glob(os.path.join(directory, '*.xls'))
dfs = []

for file in html_files:
    print(f"Processing file: {file}")
    with open(file, 'r', encoding='latin-1') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        table = soup.find('table', {'id': '_ctl0_ContentPlaceHolder1_dgResultado'})
        if table:
            df = pd.read_html(str(table), header=0)[0]
            dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
combined_df.dropna(how='all', inplace=True)

combined_df.to_excel("data/dataframe.xlsx", index=False)
