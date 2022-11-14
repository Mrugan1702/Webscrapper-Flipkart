import requests
import pandas as pd
from bs4 import BeautifulSoup
import random

def extractReviews(reviewUrl, pagenumber):
    resp = requests.get(reviewUrl)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'container'})
    #print(reviews)
    for item in reviews:
      with open('outputs/file.html', 'w') as f:
        f.write(str(item))
      
      review = {

           'Review Title': item.find('p', {'class': '_2-N8zT'}).text.split()  ,
           'Rating':item.find('div', {'class': '_3LWZlK _1BLPMq'}.text.split()) ,
           'Review Body': item.find('div', {'class': 't-ZTKy'}).text.slip() ,
      } 
      print(review)
      break
    

               


def main():

   pagenumber = 1
   productUrl = input('Paste the link of the Product Reviews page here:\n ')
   reviewUrl = productUrl.replace("/p/", "/product-reviews/" ) + "%3Fpagenumber%3D2&page=" + str(pagenumber)
   extractReviews(reviewUrl, pagenumber)




main()
