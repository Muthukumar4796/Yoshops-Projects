from urllib import request
from bs4 import BeautifulSoup
from autoscraper import AutoScraper
import requests
import csv
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Website=input("Enter the Website:")
# Category=input("Enter the Category/Subcategory:")

Category="Toys"
url="https://yoshops.com/t/"+Category.lower()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


r = requests.get(url,headers=headers)
r.status_code
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('ul', attrs = {'id':'page-cat-list'})
ch=table.find_all('li')

cat=[]
sub_cat=[]
link1=[]

# Toy category

y=ch[0].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(1,6))
cat=cat+cat1

for i in range(1,6):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)
#For mobile category
y=ch[6].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(7,11))
print(cat1)
cat=cat+cat1

for i in range(7,11):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)

# for laptop  category
y=ch[11].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(12,17))
cat=cat+cat1

for i in range(12,17):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)
# for accessories category
y=ch[17].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(18,26))
cat=cat+cat1

for i in range(18,26):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)

# for electronics category
y=ch[26].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(27,29))
cat=cat+cat1

for i in range(27,29):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)
# for home&kitchen category
y=ch[29].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(30,32))
cat=cat+cat1

for i in range(30,32):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)

#for fashion category
y=ch[32].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(33,45))
cat=cat+cat1

for i in range(33,45):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)

# for food category
y=ch[45].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(46,51))
cat=cat+cat1

for i in range(46,51):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)

y=ch[51].find('a',href=True)
x=y.text.strip()
cat1=[x]*len(range(52,64))
cat=cat+cat1

for i in range(52,64):
    y=ch[i].find('a',href=True)
    x1=y['href']
    link1.append(x1)
    x=y.text.strip()
    sub_cat.append(x)
print(sub_cat)
print(link1)


url1=[]
for link2 in link1:
    x="https://yoshops.com"+link2
    url1.append(x)
    i=i+1

x=[]
for i in range(len(url1)):
    wanted_list= ["Sony PlayStation PS2 Gaming Console 150 GB Hard Disk With 50 Games Preloaded(Black)","₹8,999.00"]
    scraper = AutoScraper()
    result = scraper.build(url1[0],wanted_list)
    mobile=scraper.get_result_similar(url1[i],grouped=True)
    mobile_list = pd.DataFrame(mobile)
    x.append(len(mobile_list))

df = pd.DataFrame({'Category': cat,'Sub-Category': sub_cat,'Number of Products': x})

df['Number of Products'].iloc[13]=df['Number of Products'].iloc[14]+df['Number of Products'].iloc[15]+df['Number of Products'].iloc[16]
df['Number of Products'].iloc[22]=df['Number of Products'].iloc[23]+df['Number of Products'].iloc[24]+df['Number of Products'].iloc[25]+df['Number of Products'].iloc[26]
df['Number of Products'].iloc[27]=df['Number of Products'].iloc[28]+df['Number of Products'].iloc[29]+df['Number of Products'].iloc[30]
df['Number of Products'].iloc[31]=df['Number of Products'].iloc[32]+df['Number of Products'].iloc[33]

df.to_excel("Category_data_Yoshops.xlsx",index=True)