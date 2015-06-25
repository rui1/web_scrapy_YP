# -*- coding: utf-8 -*-

# Scrapy settings for web_scrapy_YP project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'web_scrapy_YP'

SPIDER_MODULES = ['web_scrapy_YP.spiders']
NEWSPIDER_MODULE = 'web_scrapy_YP.spiders'
CONCURRENT_REQUESTS_PER_DOMAIN = 3
RETRY_TIMES = 10
DOWNLOAD_DELAY = 6
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True
RANDOMIZE_DOWNLOAD_DELAY = True
LOG_LEVEL = 'INFO'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'web_scrapy_YP (+http://www.yourdomain.com)'
