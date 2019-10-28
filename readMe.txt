The whole project is executed with 3 scripts.

1) First, to get all categories, sub-categories and sub-sub-categories on costco website, I go on their site-map and scrap that.
I also save it in a tab separated csv file called 'siteMap.csv'.

This is achieved by running the following script
python3 crawlCite.py

2) Once this is done, now we will visit every sub-sub-category page, and extract links of every product there. These are saved in
another file called 'allProductLinks.csv'. For simplicity, i just crawled for the first sub-sub-category.

This can be run with following command
python3 getProductLinks.py

3) After that you can run the scrape data which will read all products one by one, and extract its data.

Run the script with following command

python3 scrapeProductInfo.py

Following details, if present on product link page, are scrapped.

1) Product Name
2) Prodcut Rating
3) Download Product Image
4) Product category
5) Product Price
6) Product Delivery Date
7) Product Details
8) Remaining details of product(vary from product to product)


PFA the screen shots from running every step.
