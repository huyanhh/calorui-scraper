import scrapy
from scrapy.selector import Selector

url = "https://uci.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=3056&PeriodId=49&MenuDate=2017-05-04&Mode=day&UIBuildDateFrom=2017-05-04"

class AnteaterySpider(scrapy.Spider):
    name = "anteatery_spider"
    start_urls = [url]

    def parse(self, response):
        locator = ".menu-name"

        for menu_item in response.css(locator):
            item_locator = "a::attr(data-content)"
            item_html = menu_item.css(item_locator).extract_first()
            if not item_html:
                yield {"title": menu_item.css("span::text").extract_first()}
                continue
            selector = Selector(text=item_html)
            yield {
                "title": selector.css(".title::text").extract_first(),
                "description": selector.css(".description::text").extract_first(),
                "serving_size": selector.css("")
            }