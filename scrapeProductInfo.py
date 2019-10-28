from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from requests import get
import pandas as pd
import time

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def main():

    # set some parameters for chrome driver
    chrome_options = Options()

    # initialize chrome driver instance
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"chromedriver")

    allProductInfo = pd.read_csv('allProductLinks.csv', sep='\t')
    for index, row in allProductInfo.iterrows():
        print('Checking ', row['Category_Name'], '==>', row['Sub_Category_Name'], '==>', row['Sub_Sub_Category_Name'])
        print('Getting Information for : ', row['Product_Links'])
        # open product page
        driver.get(row['Product_Links'])
        time.sleep(5)

        try:
            # get product name
            productName = driver.find_element_by_css_selector('div.product-h1-container.visible-xs-block.visible-sm-block.visible-md-block.visible-lg-block')
            productName = productName.find_element_by_tag_name('h1')
            productName = productName.get_attribute('innerHTML')
            print('Product Name: ', productName)
        except:
            pass

        # get product rating
        try:
            ratingDiv = driver.find_element_by_id('header-bazaar-voice')
            allmetaTags = ratingDiv.find_elements_by_tag_name('meta')[0]
            rating = float(allmetaTags.get_attribute('content'))
            print('Product Rating: ',rating)
        except:
            pass

        # get product image
        try:
            productImage = driver.find_element_by_xpath('//*[@id="productImage"]').get_attribute('src')
            download(productImage, productName + '.jpg')
            print("Product Image Downloaded Successfully!!")
        except:
            pass

        try:
            # get product category
            category_hierarchy = []
            productCategory = driver.find_element_by_xpath('//*[@id="crumbs_ul"]')
            allCategories = productCategory.find_elements_by_tag_name('li')
            for category in allCategories:
                category_hierarchy.append(category.text)
            print("Product Category : " + ' >> '.join(category_hierarchy))
        except:
            pass

        try:
            # get product price
            priceHolder = driver.find_element_by_css_selector('div.your-price.row.no-gutter')
            priceHolder = priceHolder.find_element_by_css_selector('div.pull-right')
            priceHolder = priceHolder.find_element_by_css_selector('span.value').text
            print('Product Price: ', priceHolder + '$')
        except:
            pass

        try:
            # get Delivery approximation
            deliveryApproax = driver.find_element_by_css_selector('div.messages')
            deliveryApproax = deliveryApproax.find_element_by_css_selector('p.primary-clause')
            print(deliveryApproax.text)
        except:
            pass

        # get product details
        try:
            getMoreDetails = driver.find_element_by_xpath('//*[@id="view-more"]/div/input').click()
        except:
            pass
        allDetails = {}
        productDetails = driver.find_element_by_css_selector('div.accordion.panel-group').text
        productDetails = productDetails.split('\n\n')
        for productDetail in productDetails:
            productDetail = productDetail.split('\n')
            allDetails[productDetail[0]] = productDetail[1:]

        for key in allDetails.keys():
            print('\n')
            data = allDetails[key]
            print(key + ":")
            print('\n'.join(data))


    driver.close()

if __name__ == '__main__':
    main()

