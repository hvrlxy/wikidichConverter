import fpdf

class GeneratePDF():
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
        self.pdf = fpdf.FPDF() # create a pdf object

        # add arial font
        self.pdf.add_font('Arial', '', 'arial.ttf', uni=True)  # added line
        self.output_book_cover() # output the book cover
        self.output_all_chapter() # output all chapter

    def output_book_cover(self):
        '''
        Generate the pdf page for the book cover
        return: None
        '''
        # Add a page
        self.pdf.add_page() # added new page

        # set font to bold
        self.pdf.set_font("Arial", size = 15, style='B') # added Arial, as a font, set to bold
        self.pdf.cell(self.width, self.height, txt = self.book_name, ln = 1, align = "C") # added cell, with book name
    
    def output_chapter(self, chapter_text, chapter_num):
        '''
        Generate the pdf page for a chapter
        chapter_text: str
        chapter_num: int
        return: None
        '''
        # Add a page
        self.pdf.add_page() # added new page
        # set font to bold
        self.pdf.set_font("Arial", size = 15, style='B') # added Arial, as a font, set to bold
        # create a cell
        self.pdf.cell(self.width, self.height, txt = 'Chapter ' + str(chapter_num), ln = 1, align = "C") # added cell, with chapter number

        # unset font to normal
        self.pdf.set_font("Arial", size = 15, style='') # added Arial, as a font, set to normal
        self.pdf.multi_cell(self.width, self.height, txt = chapter_text,
                border = 0, align = 'L', fill = False) # added multi_cell, with chapter text

    def output_all_chapter(self):
        '''
        Generate the pdf page for all chapters
        return: None
        '''
        for i in range(len(self.chapter_list)): # i + 1 is the chapter index
            self.output_chapter(self.chapter_list[i], i + 1) # output the chapter

    def save_pdf(self, filename):
        '''
        Save the pdf file
        filename: str
        return: None
        '''
        # save the pdf with name .pdf
        self.pdf.output(filename) # added output, with filename