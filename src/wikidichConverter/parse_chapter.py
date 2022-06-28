from bs4 import BeautifulSoup
import requests
import random
from time import sleep

class ParseChapter:
    def __init__(self, url) -> None:
        self.url = url 
        self.webpage_soup = self.get_webpage()

    def get_webpage(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        return soup 

    def get_chapter_paragraphs(self):
        chapter_div = self.webpage_soup.find("div", {"id": "bookContentBody"})
        paragraphs = []
        for child in chapter_div.findChildren("p" , recursive=False):
            paragraphs.append(child)
        return paragraphs

    def get_paragraph_contents(self, paragraph):
        return paragraph.text

    def get_chapter_text(self):
        ps = self.get_chapter_paragraphs()
        text = ''
        for p in ps:
            text += (self.get_paragraph_contents(p))
            text += '\n'
        return text

    def get_next_chapter(self, index):
        list1 = [3, 4, 5, 6]
        sleep(random.choice(list1))
        ankhito_div = self.webpage_soup.find("div", {"class": "ankhito center"})
        btns = ankhito_div.findChildren('a')
        print(btns)
        try:
            return 'https://wikidth.net/' + btns[index].get('href')
        except:
            return None
        


