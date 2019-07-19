Scrapy Practice
=========================

A practice scrapy project modified from a [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3).

### Usage

This scrapy project parses the Brickset website to get information of the Lego products which were first sold in the year of 2016.

### Output

* name
* pieces
* minifigs

Name|Pieces|Minifigs
-|-|-
Brick Bank|2380|5
Volkswagen Beetle|1167|-
Big Ben|4163|-

### Running the spider

Run the spider using the `scrapy crawl` command:

    $ scrapy crawl brickset

A csv file titled 'brickset.csv' will be generated in the 'brickset' root folder.

### Requirements

* Python
* Scrapy