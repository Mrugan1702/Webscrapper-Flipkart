import requests
import pandas as pd
from bs4 import BeautifulSoup
import random


reviewlist = []

 
def extractReviews(reviewUrl, i):
    resp = requests.get(reviewUrl)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'_1YokD2 _3Mn1Gg col-9-12'})
    # print(reviews)
    for item in reviews:
        with open('outputs/file.html', 'w', encoding='utf-8') as f:
            f.write(str(item))
        
        review = {
            'Review Title': item.find('p', {'_2-N8zT'}).text.strip(),
            'Rating': item.find('div', {'_3LWZlK _1BLPMq'}).text.strip(),
            'Review Body': item.find('div', {'t-ZTKy'}).text.strip() ,
        }
        reviewlist.append(review)  

def totalPages(productUrl):
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find('div', {'col-12-12'})
    return int(reviews.text.strip().split(', ')[1].split(" ")[0])

def main():
    productUrl = "https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&iid=1b712a17-d1a6-4946-a3f1-5768c526981f.MOBFWQ6BXGJCEYNY.SEARCH&ssid=o09q4rvzcw0000001668327784891&qH=0b3f45b266a97d70"
    reviewUrl = productUrl.replace("/p/", "/product-reviews/" ) + "%3Fpagenumber%3D2&page=" + str(1)
    totalPg = totalPages(reviewUrl)
    print(totalPg)

for i in range(totalPg//10):
        print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl.replace("dp", "product-reviews") + "?pageNumber=" + str(i)
            extractReviews(reviewUrl, i)
        except Exception as e:
            print(e)

            df = pd.DataFrame(reviewlist)
    df.to_csv('output.csv', index=False)



main()