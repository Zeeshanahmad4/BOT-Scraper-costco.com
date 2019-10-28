from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

def main():

    # set some parameters for chrome driver
    chrome_options = Options()

    # initialize chrome driver instance
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"chromedriver")

    # open product page
    driver.get("https://www.costco.com/SiteMapDisplayView")
    time.sleep(3)

    Category_Name = []
    Category_Link = []
    Sub_Category_Name = []
    Sub_Category_Link = []
    Sub_Sub_Category_Name = []
    Sub_Sub_Category_Link = []

    all_categories = driver.find_elements_by_css_selector('div.col-xs-12.sitemap-section')
    for category in all_categories:
        categoryTag = category.find_element_by_css_selector('a.h2-style-guide')
        categoryName = categoryTag.get_attribute('innerHTML')
        categoryLink = categoryTag.get_attribute('href')
        print("Currently In Category: ", categoryName, categoryLink)

        subcategory = category.find_element_by_css_selector('ul.row.hidden-xl')
        subcategory_containers = subcategory.find_elements_by_css_selector('li.col-sm-6.hidden-xl')
        for subcategory_container in subcategory_containers:
            allsublistlistitems = subcategory_container.find_elements_by_tag_name('li')
            for allsublistlistitem in allsublistlistitems:
                try:
                    subcategoryTag = allsublistlistitem.find_element_by_css_selector('a.body-copy-link')
                except:
                    continue
                subcategoryName = subcategoryTag.get_attribute('innerHTML')
                subcategoryLink = subcategoryTag.get_attribute('href')
                print("Currently In Sub_Category: ", subcategoryName, subcategoryLink)
                try:
                    subsubcatrgoryList = allsublistlistitem.find_element_by_css_selector('ul.sub-list')
                except:
                    continue
                subsubcatrgoryLists = subsubcatrgoryList.find_elements_by_tag_name('li')
                for subsubcateogry in subsubcatrgoryLists:
                    subsubcategoryTag = subsubcateogry.find_element_by_tag_name('a')
                    subsubcategoryName = subsubcategoryTag.get_attribute('innerHTML')
                    subsubcategoryLink = subsubcategoryTag.get_attribute('href')
                    print("Currently In Sub_Sub_Category: ", str(subsubcategoryName), subsubcategoryLink)
                    Category_Name.append(categoryName)
                    Category_Link.append(categoryLink)
                    Sub_Category_Name.append(subcategoryName)
                    Sub_Category_Link.append(subcategoryLink)
                    Sub_Sub_Category_Name.append(subsubcategoryName)
                    Sub_Sub_Category_Link.append(subsubcategoryLink)

    data = pd.DataFrame({
        'Category_Name':Category_Name,
        'Category_Link':Category_Link,
        'Sub_Category_Name':Sub_Category_Name,
        'Sub_Category_Link':Sub_Category_Link,
        'Sub_Sub_Category_Name':Sub_Sub_Category_Name,
        'Sub_Sub_Category_Link':Sub_Sub_Category_Link
    })

    data.to_csv('siteMap.csv', sep="\t")

    driver.close()

if __name__ == '__main__':
    main()
