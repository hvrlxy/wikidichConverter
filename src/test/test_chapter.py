from wikidichConverter.parse_chapter import *
import pytest

chapter_text = open('test_cases/test_chapter_text.txt', 'r').read()

def test_chapter_text():
    url  = 'https://wikidth.net/truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co/chuong-35-chuong-35-YcT1HsQsRFqxnmY4'
    obj = ParseChapter(url)
    text = obj.get_chapter_text()
    assert text == chapter_text

def test_next_chapter():
    url  = 'https://wikidth.net/truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co/chuong-35-chuong-35-YcT1HsQsRFqxnmY4'
    obj = ParseChapter(url)
    assert (obj.get_next_chapter()) == 'https://wikidth.net//truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co/chuong-36-chuong-36-YcT1HsQsRFqxnmY5'

