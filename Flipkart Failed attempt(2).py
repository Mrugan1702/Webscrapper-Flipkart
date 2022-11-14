import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.flipkart.com/poco-f1-graphite-black-64-gb/product-reviews/itmf8fyjyssnt25c?page={}&pid=MOBF85V7A6PXETAX"
driver = webdriver.Chrome(executable_path='Users/mrugankulkarni/Desktop/chromedriver.exe')
for page_num in range(1,5):
    driver.get(link.format(page_num))
    [item.click() for item in driver.find_elements_by_class_name("_1EPkIx")]
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for items in soup.select("._3DCdKt"):
        title = items.select_one("p._2xg6Ul").text
        review = ','.join(items.select_one(".qwjRop div:nth-of-type(2)").text.split())
        with open("/Users/mrugankulkarni/Documents/Vscode/TestProject01/result.csv","w") as file:
            file.write(review)

driver.quit()