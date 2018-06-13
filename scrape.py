from bs4 import BeautifulSoup
import urllib

def get_image_link(id):    
    anime_url = 'https://myanimelist.net/anime/' + str(id) + '/'
    req = urllib.urlopen(anime_url).read()
    
    soup = BeautifulSoup(req, 'html.parser')
    image_div = soup.findAll('img', class_ = 'ac')
    src = ''

    try:
        src = image_div[0]['src']
    except IndexError:
        pass

    return src