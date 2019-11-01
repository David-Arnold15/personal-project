import requests as rq
from bs4 import BeautifulSoup as bs
def table_scrape(website, debug):
    if debug == False:
        #makes an  html request to the given site
        r = rq.get(website, verify=False)
        html_doc = r.content
    else: 
        pass;
    soup = bs(html_doc, 'html.parser')
    actor_table = soup.find_all('td', class_ = 'primary_photo' )
    actors = []
    #print(bs.get_text(actor_table[0].findNextSibling('td')))
    #adds every actor to a list
    for i in range(len(actor_table)):
        actors.append(bs.get_text(actor_table[i].findNextSibling('td')))
    #removes whitespace characters
    for i in range(len(actors)):
        actors[i] = actors[i].strip()
    #print(actors)    
    return actors
                   
        
        
if __name__ == "__main__":
    print(table_scrape("https://www.imdb.com/title/tt2250912/?ref_=nv_sr_3?ref_=nv_sr_3", False))
