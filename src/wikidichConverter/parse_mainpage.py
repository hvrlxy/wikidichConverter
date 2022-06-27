from ast import excepthandler
from bs4 import BeautifulSoup
import requests

class ParseMainPage:
    def __init__(self, url) -> None:
        self.url = url 
        self.webpage_soup = self.get_webpage()
    
    def get_webpage(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        return soup

    def get_first_chapter(self):
        try:
            read_btn = self.webpage_soup.find("a", {"class": "btn waves-effect waves-light orange-btn"})
            return 'https://wikidth.net/' + read_btn.get('href')
        except:
            return None

    def get_book_name(self):
        cover_info = self.webpage_soup.find("div", {"class": "cover-info"})
        h2 = cover_info.findChildren("h2")
        return h2[0].text