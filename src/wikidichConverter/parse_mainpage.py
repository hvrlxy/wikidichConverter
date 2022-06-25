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
        read_btn = self.webpage_soup.find("a", {"class": "btn waves-effect waves-light orange-btn"})
        return 'https://wikidth.net/' + read_btn.get('href')

#test
obj = ParseMainPage('https://wikidth.net/truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co-Ya2smlS4CFNOCent#!')
print(obj.get_first_chapter())