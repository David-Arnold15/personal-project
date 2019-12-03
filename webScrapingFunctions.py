import requests as rq
from bs4 import BeautifulSoup as bs
website = ""
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
        #follow a link off of the primary photo and get the images from it
        link = actor_table[i].parent
        print(link)
        actors.append(bs.get_text(actor_table[i].findNextSibling('td')))
    #removes whitespace characters
    for i in range(len(actors)):
        actors[i] = actors[i].strip()
    #print(actors)    
    
    #get the images of these actors
    return actors
                   
        
        
if __name__ == "__main__":
    website = input("please paste an imdb link for the movie you wish to watch: ")
    print(table_scrape("https://www.imdb.com/title/tt4154756/?ref_=nv_sr_1?ref_=nv_sr_1" , False))
