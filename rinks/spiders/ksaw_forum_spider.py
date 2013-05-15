from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from rinks.items import RinksItem
from rinks.variables import Currency_Regex

class KsawForumSpider(BaseSpider):
	name = "ksaw"
	allowed_domains = ["http://iceforum.com"]
	start_urls = ["http://www.iceforum.com/Page.asp?n=24865"]


	def parse(self,response):
		hxs = HtmlXPathSelector(response)

		link = "http://www.iceforum.com/Page.asp?n=24865"
		cost = hxs.select("//div[@id='editArea24865']/div[3]/span/span/text()").re(Currency_Regex)


		rows = hxs.select("//*[@id='editArea24865']/div[4]/table/tbody/tr")

		items = []

		i = 0
		for row in rows:
			if i != 0:
				item = RinksItem()
				item['link'] = link
				item['cost'] = cost
				item['day'] = row.select("td[1]//*/text()").extract()
				item['date'] = row.select("td[2]//*/text()").extract()
				item['time'] = row.select("td[3]//*/text()").extract()
				items.append(item)
			i += 1

		return items