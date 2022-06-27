import parse_mainpage
import generate_pdf
import parse_chapter

def get_all_chapter(url):
    mainpage = parse_mainpage.ParseMainPage(url)
    chapter_url = mainpage.get_first_chapter()
    chapter_text_lst = []

    while chapter_url is not None:
        chapter = parse_chapter.ParseChapter(chapter_url)
        chapter_text_lst.append(chapter.get_chapter_text())
        chapter_url = chapter.get_next_chapter(1) if len(chapter_text_lst) == 1 else chapter.get_next_chapter(2)
        print(chapter_url)
    return chapter_text_lst

book_url = 'https://wikidth.net/truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co-Ya2smlS4CFNOCent#!'
book_name = parse_mainpage.ParseMainPage(book_url).get_book_name()
chapter_text_lst = get_all_chapter(book_url)
print(len(chapter_text_lst))
obj = generate_pdf.GeneratePDF(chapter_text_lst, book_name)
obj.save_pdf('test.pdf')