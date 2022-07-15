from wikidichConverter.parse_mainpage import *
from wikidichConverter.generate_files import *
from wikidichConverter.parse_chapter import *
import os

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

def convert_pdf(markdown_path: str, output_file: str):
    '''
    Convert a book url to a pdf file
    book_url: str
    file_path: str
    '''

    os.system(f"pandoc --pdf-engine=xelatex -V CKJmainfont=arial {markdown_path} -o {output_file}")  


def convert_md(book_url: str, markdown_path: str):
    '''
    Convert a book url to a md file
    book_url: str
    file_path: str
    '''

    book_name = ParseMainPage(book_url).get_book_name() # get the book name
    chapter_text_lst = get_all_chapter(book_url) # get all chapter text
    obj = GenerateFile(chapter_text_lst, book_name) # generate the md file
    obj.save_md(markdown_path)

def convert_epub(markdown_path: str, file_path: str):
    '''
    Convert a book url to a epub file
    book_url: str
    file_path: str
    '''

    pypandoc.convert_file(markdown_path, 'epub', outputfile=file_path)