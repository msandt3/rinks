RINK SCRAPING
=============

Proof of concept for scraping data from in the wild rink websites

How to Run
----------

After cloning this repository you can run the scraping routines:

	$ scrapy crawl ice

One can also store the data from scraping in item pipeline files, these commands will store the items in JSON CSV and XML format respectively:

	$ scrapy crawl ice -o items.json -t json
	$ scrapy crawl ice -o items.csv -t csv
	$ scrapy crawl ice -o items.xml -t xml

For more information on how to use Scrapy please see the [Scrapy Reference][1]

[1]: http://doc.scrapy.org/en/latest/index.html

