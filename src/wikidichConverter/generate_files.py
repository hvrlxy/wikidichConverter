from email import header
import fpdf
from wikidichConverter import *
import os
import markdown_strings as ms
import pypandoc
from mdutils.mdutils import MdUtils
from mdutils import Html

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class GenerateFile():
    def __init__(self, chapters_list, book_name): 
        '''
        Constructor
        chapters_list: list of str
        book_name: str
        '''
        self.width = 180 # width of the cell
        self.height = 12 # height of the cell
        self.book_name = book_name.encode('latin-1', 'replace').decode('latin-1') # encode book name
        self.chapter_list = chapters_list # list of chapter text

    def save_md(self, file_name):
        '''
        Save the md file
        return: None
        '''
        # save the md file
        mdFile = MdUtils(file_name=file_name, title=self.book_name)

        for i in range(len(self.chapter_list)):
            mdFile.new_header(level=1, title=f'Chapter {i+1}')
            texts = self.chapter_list[i].split('\n')
            for text in texts:
                mdFile.new_paragraph(text)
            mdFile.write('\n') 

        mdFile.new_table_of_contents(table_title='Table of Contents', depth=2)
        mdFile.create_md_file()       

    def save_pdf(self, markdown_file, output_file):
        '''
        Save the pdf file
        filename: str
        return: None
        '''
        pypandoc.convert_file(markdown_file, 'pdf', outputfile=output_file)

    def save_epub(self, markdown_file, output_file):
        '''
        Save the epub file
        filename: str
        return: None
        '''
        pypandoc.convert_file(markdown_file, 'epub', outputfile=output_file)