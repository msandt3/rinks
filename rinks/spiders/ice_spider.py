from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from rinks.items import RinksItem

class IceSpider(BaseSpider):
	name = "ice"
	allowed_domains = ["http://theice.info"]
	start_urls = ["http://theice.info/Live/default.html"]


	""" This method parses the ice's url """
	def parse(self,response):
		hxs = HtmlXPathSelector(response)

		""" Set Up an Item and Populate Fields"""
		container = hxs.select("//div[@class='gbox']/div[2]/span")

		days = self.makelist(container.select("text()[1]").extract()[0])
		items = []

		for day in days:
			item = RinksItem()
			item['link'] = "http://theice.info"
			item['day'] = day
			item['time'] = self.stripwhitespace(container.select("text()[2]").extract()[0])
			item['cost'] = "N/A"
			item['date'] = "N/A"
			items.append(item)
		return items


	def stripwhitespace(self,item):
		item = item.replace(" ","")
		item = item.replace("\n","")
		return item

	def makelist(self,items):
		items = self.stripwhitespace(items)
		newlist = items.split(",")
		return newlist

