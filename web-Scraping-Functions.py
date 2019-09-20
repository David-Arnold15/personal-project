import requests as rq
from bs4 import BeautifulSoup as bs
def table_scrape(website):
    r = rq.get(website, verify=False)
    html_doc = ''
    soup = bs(html_doc, 'html.parser')
    print(r.text)
    
table_scrape("http://www.bing.com")