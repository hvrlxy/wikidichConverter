import fpdf

chapter_text = open('../test/test_cases/chapter_text.txt', 'r').read()

class GeneratePDF():
    def __init__(self, chapters_list, book_name): 
        self.width = 180
        self.height = 12
        self.book_name = book_name.encode('latin-1', 'replace').decode('latin-1')
        self.chapter_list = chapters_list
        self.pdf = fpdf.FPDF()

        # add arial font
        self.pdf.add_font('Arial', '', 'arial.ttf', uni=True)  # added line
        self.output_book_cover()
        self.output_all_chapter()

    def output_book_cover(self):
        # Add a page
        self.pdf.add_page()

        # set font to bold
        self.pdf.set_font("Arial", size = 15, style='B')
        self.pdf.cell(self.width, self.height, txt = self.book_name, ln = 1, align = "C")
    
    def output_chapter(self, chapter_text, chapter_num):
        # Add a page
        self.pdf.add_page()
        # set font to bold
        self.pdf.set_font("Arial", size = 15, style='B')
        # create a cell
        self.pdf.cell(self.width, self.height, txt = 'Chapter ' + str(chapter_num), ln = 1, align = "C")

        # unset font to normal
        self.pdf.set_font("Arial", size = 15, style='')
        self.pdf.multi_cell(self.width, self.height, txt = chapter_text,
                border = 0, align = 'L', fill = False)

    def output_all_chapter(self):
        for i in range(len(self.chapter_list)):
            self.output_chapter(self.chapter_list[i], i + 1)

    def save_pdf(self, filename):
        # save the pdf with name .pdf
        self.pdf.output(filename)  