import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

# List to store data
data_list = []    


# Create the Spider class
class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
                # get titles, prices,and ratings
                title = response.css("h3 a::attr(title)").extract()
                price = response.css("p.price_color::text").extract()
                ratings = response.css("p.star-rating::attr(class)").extract()
               
                for title, price,rate in zip(title, price,ratings):
                          data_list.append({
                                  "title": title.strip(),
                                  "price": price.strip(),
                                  "rating": rate.strip()
                                    })
                next_page = response.css("li.next a::attr(href)").get()
                if next_page:
                      yield response.follow(next_page, callback=self.parse)
 
#Run the Spider       
process = CrawlerProcess() 
process.crawl(BooksSpider) 
process.start() 

df = pd.DataFrame(data_list) # convert the list to a DataFrame
print(df.head()) #show the first few rows of the DataFrame

df.to_csv("books.csv", index=False) #make a CSV file
df.to_excel("books.xlsx", index=False, engine="openpyxl") #save to excel file

