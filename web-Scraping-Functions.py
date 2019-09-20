import requests as rq
from bs4 import BeautifulSoup as bs
def table_scrape(website, debug):
    if debug == False:
        r = rq.get(website, verify=False)
        html_doc = r.content
    else: 
        f= open("imdbpage.txt","w+")
        html_doc = f
    soup = bs(html_doc, 'html.parser')
    actor_table = soup.find_all('td', class_ = 'primary_photo' )
    print(actor_table[0].findNextSibling('td'))
table_scrape("https://www.imdb.com/title/tt4154756/?ref_=nv_sr_1?ref_=nv_sr_1", False)
