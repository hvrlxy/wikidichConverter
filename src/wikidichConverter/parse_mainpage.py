from ast import excepthandler
from bs4 import BeautifulSoup
import requests

class ParseMainPage:
    def __init__(self, url) -> None:
        '''
        Constructor
        url: str
        '''
        self.url = url # url of the main page
        self.webpage_soup = self.get_webpage() # get the webpage
    
    def get_webpage(self):
        '''
        Get the webpage from the url
        return: BeautifulSoup object
        '''
        req = requests.get(self.url) # get the webpage
        soup = BeautifulSoup(req.content, 'html.parser') # parse the webpage

        return soup

    def get_first_chapter(self):
        '''
        Get the url of the first chapter
        return: str
        '''
        # find the first chapter link, for some of the book, there are no chapter available (yet)
        try:
            read_btn = self.webpage_soup.find("a", {"class": "btn waves-effect waves-light orange-btn"}) # find the read button
            return 'https://wikidth.net/' + read_btn.get('href') # get the url of the first chapter
        except:
            return None

    def get_book_name(self):
        '''
        Get the name of the book
        return: str
        '''
        cover_info = self.webpage_soup.find("div", {"class": "cover-info"}) # find the cover info div
        h2 = cover_info.findChildren("h2") # find the h2 tag
        return h2[0].text # get the book name