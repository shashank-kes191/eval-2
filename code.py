from bs4 import BeautifulSoup 
import requests
import pandas as pd
#from pymongo import MongoClient
df = pd.read_csv('data.csv.csv')
#client = MongoClient('mongodb://localhost:27017/')
#db = client['test']
#collection = db['eval']
newdf = df[df['City/Town'] == 'ALICE' & df['start_date'] >= "01-01-2010" & df['end_date'] <= "01-01-2022"]
print(newdf['Provider Name'])
newdf2 = df[df['STATE'] == 'GA']
print(newdf2['SCORE'].count())
collection.update_many({'CMS Region': '4', 'Telephone Number': '(334) 493-3541'},{'$set': {'Telephone': '(444) 456-3555'}})
