from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

def main():

    # set some parameters for chrome driver
    chrome_options = Options()

    # initialize chrome driver instance
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"chromedriver")

    Category_Name = []
    Category_Link = []
    Sub_Category_Name = []
    Sub_Category_Link = []
    Sub_Sub_Category_Name = []
    Sub_Sub_Category_Link = []
    Product_Links = []

    siteMap = pd.read_csv('siteMap.csv', sep='\t')
    for index, row in siteMap.iterrows():

        print('Checking ', row['Category_Name'], '==>', row['Sub_Category_Name'],'==>',row['Sub_Sub_Category_Name'])
        # open product page
        driver.get(row['Sub_Sub_Category_Link'])
        time.sleep(5)
        allProducts = driver.find_elements_by_css_selector('div.product-tile-set')
        for productLink in allProducts:
            link = productLink.get_attribute('data-pdp-url')
            print(link)
            Product_Links.append(link)
            Category_Name.append(row['Category_Name'])
            Category_Link.append(row['Category_Link'])
            Sub_Category_Name.append(row['Sub_Category_Name'])
            Sub_Category_Link.append(row['Sub_Category_Link'])
            Sub_Sub_Category_Name.append(row['Sub_Sub_Category_Name'])
            Sub_Sub_Category_Link.append(row['Sub_Sub_Category_Link'])



    driver.close()

    data = pd.DataFrame({
        'Category_Name': Category_Name,
        'Category_Link': Category_Link,
        'Sub_Category_Name': Sub_Category_Name,
        'Sub_Category_Link': Sub_Category_Link,
        'Sub_Sub_Category_Name': Sub_Sub_Category_Name,
        'Sub_Sub_Category_Link': Sub_Sub_Category_Link,
        'Product_Links': Product_Links
    })

    data.to_csv('allProductLinks.csv', sep='\t')

if __name__ == '__main__':
    main()
