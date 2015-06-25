__author__ = 'rui'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from web_scrapy_YP.items import YPItem
from yp_util import *
import sys


class YPSpider(CrawlSpider):
    name = "YP"
    #logfile = open('testlog.log', 'w')
    #log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
    #log_observer.start()

    allowed_domains = ['www.yellowpages.com']
    k = ['search_terms','geo_location_terms']
    params={}
    for i in range(len(k)):
        v = raw_input('Enter the %s to search on YP:'%k[i])
        if v=='exit':
            sys.exit()
        params[k[i]]=v

    print 'Scraping...'
    print 'Your log file is saved in scrapy_outlog.log. '
    root_url = 'http://www.yellowpages.com/search'
    start_urls=[addParamToUrl(root_url,params)]
    rules = (
    Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination"]'), callback='parse_items_YP',follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_items_YP(response)
    def parse_items_YP(self,response):
        items=[]
        if response.status !=200:
            return items
        for sel in response.xpath("//div[@class='search-results organic']//div[@class='v-card']"):
            item = YPItem()
            item['YPimglink']=sel.xpath("div[@class='media-thumbnail']/a/img/@src").extract()

            infosel = sel.xpath("div[@class='info']")
            rank = infosel.xpath("h3[@class='n']/text()").extract()
            if len(rank)==0:
                rank = ['0']
            else:
                rank=custom_strip(rank)
            item['YPrank']=rank

            item['menuLink']=[self.allowed_domains[0]+x for x in infosel.xpath("h3/a[@class='menu']/@href").extract()]
            item['businessName']=custom_strip(infosel.xpath("h3/a[@class='business-name']/text()").extract())

            infoPrim = infosel.xpath("div[@class='info-section info-primary']")
            review= infoPrim.xpath("a[@class='rating']")
            reviewStar = custom_strip(review.xpath('div/@class').extract())
            reviewNum = custom_strip(review.xpath('div/span/text()').extract())
            item['YPreveiwStar']=[rev.split(" ")[-1] for rev in reviewStar]
            item['YPreviewNum']=reviewNum

            address = infoPrim.xpath("p/span")
            adrsSubKey = address.xpath("@itemprop").extract()
            adrsSubValue = address.xpath("text()").extract()
            for i in range(len(adrsSubKey)):
                try:
                    adrsSubValue[i]=custom_strip(adrsSubValue[i])[0]
                    item[adrsSubKey[i]]=adrsSubValue[i]
                except KeyError as e:
                    print 'got one extra field %s'% adrsSubKey
            item['addressTotal']=",".join(adrsSubValue)
            item['telephone']=infoPrim.xpath("div[@class='phones phone primary']/text()").extract()

            infoScnd = infosel.xpath("div[@class='info-section info-secondary']")
            item['categories']=infoScnd.xpath("div[@class='categories']/a/text()").extract()

            links = infoScnd.xpath("div[@class='links']")
            linkNames = [x.lower().replace(' ','_') for x in links.xpath("a/text()").extract()]
            linkValue = links.xpath("a/@href").extract()
            for j in range(len(linkNames)):
                try:
                    if linkNames[j] in ['more_info','directions']:
                        linkValue[j]=self.allowed_domains[0]+linkValue[j]
                    item[linkNames[j]]=linkValue[j]
                except KeyError as e:
                    print "detect one extra field %s"% linkNames

            items.append(item)
        return items


