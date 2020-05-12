import scrapy 

class News_scraper(scrapy.Spider):
    name = 'news'
    start_urls = ['https://www.hindustantimes.com/coronavirus/',
                 ]
    def parse(self,response):        
        news_page_links = response.css('div.listBlock div.info a')
        yield from response.follow_all(news_page_links, self.parse_author)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        def extract_with_css_all(query):
            return response.css(query).getall()
        yield {
            'title': extract_with_css('div.storyArea h1::text'),
            'date': extract_with_css('span.text-dt::text'),
            'News': extract_with_css_all('div.storyDetail p::text'),
             #'News': extract_with_css_all('div.storyDetail p'),
        }
