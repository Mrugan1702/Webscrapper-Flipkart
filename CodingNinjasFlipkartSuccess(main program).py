import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

link=input('Paste the link of the second page of Reviews page here:\n')
page=link[-1:]
page=int(page)
for i in range(page-1,125):
    new_link=link.rstrip('2')
    i=str(i)
    output_link=new_link+i
    print(output_link)
    page=requests.get(output_link)
    page.content
    soup=BeautifulSoup(page.content,'html.parser')
    new_rev=[]
    for j in soup.find_all('div',class_="_6t1WkM _3HqJxg"):
        new_rev.append(j.text.split("."))
    
    stored = {"reviews":new_rev[0]}
    
    data=pd.DataFrame(data=stored)
    data.to_csv('Finalreviews.csv', mode='a', index=False, header=False)

    print(data)
