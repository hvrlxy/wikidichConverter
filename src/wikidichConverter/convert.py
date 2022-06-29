from wikidichConverter.parse_mainpage import *
from wikidichConverter.generate_pdf import *
from wikidichConverter.parse_chapter import *

def get_all_chapter(url: str):
    '''
    Get all chapter text from a book url
    url: str
    return: list of str
    '''
    mainpage = ParseMainPage(url) # parse the mainpage
    chapter_url = mainpage.get_first_chapter() # get the url of the first chapter
    chapter_text_lst = [] # list of chapter text

    while chapter_url is not None:
        chapter = ParseChapter(chapter_url) # parse the chapter
        chapter_text_lst.append(chapter.get_chapter_text()) # add the chapter text to the list
        chapter_url = chapter.get_next_chapter(1) if len(chapter_text_lst) == 1 else chapter.get_next_chapter(2) # get the url of the next chapter
        # print(chapter_url)
    return chapter_text_lst

def convert_pdf(book_url: str, file_path: str):
    '''
    Convert a book url to a pdf file
    book_url: str
    file_path: str
    '''

    book_name = ParseMainPage(book_url).get_book_name() # get the book name
    chapter_text_lst = get_all_chapter(book_url) # get all chapter text
    obj = GeneratePDF(chapter_text_lst, book_name) # generate the pdf file
    obj.save_pdf(file_path)