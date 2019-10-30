# BOT-Scraper-costco.com



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Zeeshanahmad4/BOT--Hydrafacial">
    <img src="https://github.com/Zeeshanahmad4/BOT--Hydrafacial/blob/master/208498-OZT9V0-402.png" alt="Logo" width="120" height="150">
  </a>
  <h3 align="center">Scraper/Bot</h3>
  <h3 align="center">Scraping Provider from <a href="https://costco.com/"> costco.com </a> </h3>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project
![Product Name Screen Shot](https://github.com/Zeeshanahmad4/BOT-Scraper-costco.com/blob/master/hjjhjjhhghgcghdhfdhgd.jpg)


### Built With
* [Python](https://www.python.org/)
* [Beautifullsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [csv](https://en.wikipedia.org/wiki/Comma-separated_values)
* [Selenium](https://en.wikipedia.org/wiki/Comma-separated_values)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* beautifulsoup
```sh
pip install bs4
pip install selenium
```


### Installation
1. Clone the repo
```sh
git clone https://github.com/Zeeshanahmad4/BOT-Scraper-costco.com.git
```
2. Install python 
```sh
install python
```
3. Install python packages
```sh
pip install bs4
```

<!-- USAGE EXAMPLES -->
## Usage
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


## Includes Files
1. crawlCite.py
2. getProductLinks.csv
3. scrapeProductInfo

<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/Zeeshanahmad4/BOT-Scraper-costco.com/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact me :

<table>
  <tr>
    <th>
      <ahref="http://zeeshanahmad.me/" >
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/edit1.jpg" alt="Logo" width="182" height="90">
 </a> </th>
    <th>
      <a href="http://zeeshanahmad.me/">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/edit2.jpg" alt="Logo" width="182" height="90">
 </a> </th>
    <th>
      <a href="http://zeeshanahmad.me/">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/edit3.jpg" alt="Logo" width="182" height="90">
 </a> </th>
    <th>
      <a href="http://zeeshanahmad.me/">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/edit4.jpg" alt="Logo" width="182  " height="90">
 </a> </th>
    </tr>
 </table>
<table>
  <tr>
    <th>
      <a href="https://www.upwork.com/freelancers/~0180a61cf01f9bc71d" >
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/download.png" alt="Logo" width="182" height="80">
 </a> </th>
    <th>
      <a href="https://www.linkedin.com/in/zeeshan-ahmad-87098b105/">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/linked-in-3200.jpg" alt="Logo" width="182" height="80">
 </a> </th>
    <th>
      <a href="https://www.kaggle.com/zeeshanahmad4">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/Kaggle_logo.png" alt="Logo" width="182" height="80">
 </a> </th>
    <th>
      <a href="https://twitter.com/Zeeshan_Ahmad6">
    <img src="https://github.com/Zeeshanahmad4/My-Path-to-Python/blob/master/multimedia/twitter-logo-png-open-2000.png" alt="Logo" width="182" height="80">
 </a> </th>
    </tr>
 </table>






