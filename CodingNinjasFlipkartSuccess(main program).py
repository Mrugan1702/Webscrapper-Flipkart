import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

link=input('Paste the link of the second page of Reviews page here:\n')
page=link[-1:]
page=int(page)
for i in range(page-1,125):
    l=link.rstrip('2')
    i=str(i)
    final=l+i
    print(final)
    page=requests.get(final)
    page.content
    soup=BeautifulSoup(page.content,'html.parser')
    review2=[]
    for j in soup.find_all('div',class_="_6t1WkM _3HqJxg"):
        review2.append(j.text.split("."))
    
    data1={"reviews":review2[0]}
    
    data=pd.DataFrame(data=data1)
    data.to_csv('output.csv', mode='a', index=False, header=False)

    print(data)