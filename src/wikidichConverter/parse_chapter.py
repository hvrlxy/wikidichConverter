from bs4 import BeautifulSoup
import requests
import random
from time import sleep

class ParseChapter:
    def __init__(self, url) -> None:
        '''
        Constructor
        url: str
        '''
        self.url = url 
        self.webpage_soup = self.get_webpage()

    def get_webpage(self):
        '''
        Get the webpage from the url
        return: BeautifulSoup object
        '''
        req = requests.get(self.url) # get the webpage
        soup = BeautifulSoup(req.content, 'html.parser') # parse the webpage

        return soup 

    def get_chapter_paragraphs(self):
        '''
        Get all paragraphs in the chapter
        return: list of BeautifulSoup object
        '''

        chapter_div = self.webpage_soup.find("div", {"id": "bookContentBody"}) # find the div that contains the chapter
        paragraphs = [] # list of paragraphs
        for child in chapter_div.findChildren("p" , recursive=False):
            paragraphs.append(child) # add the paragraph to the list
        return paragraphs

    def get_paragraph_contents(self, paragraph):
        '''
        Get the contents of a paragraph
        paragraph: BeautifulSoup object
        return: str
        '''
        return paragraph.text

    def get_chapter_text(self):
        '''
        Get the text of the chapter
        return: str
        '''

        ps = self.get_chapter_paragraphs() # get all paragraphs in the chapter
        text = '' # text of the chapter
        for p in ps:
            text += (self.get_paragraph_contents(p)) + '\n' # add the paragraph to the text
        return text

    def get_next_chapter(self, index):
        '''
        Get the url of the next chapter
        index: int
        return: str
        '''

        list1 = [1,2,3,4] # list of index of random time, used to prevent the bot from being blocked
        sleep(random.choice(list1)) # sleep for a random time
        ankhito_div = self.webpage_soup.find("div", {"class": "ankhito center"}) # find the div that contains the next chapter
        btns = ankhito_div.findChildren('a') # find all the buttons in the div
        try:
            return 'https://wikidth.net/' + btns[index].get('href') # get the url of the next chapter
        except:
            return None
        


