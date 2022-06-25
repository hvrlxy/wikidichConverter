from wikidichConverter.parse_mainpage import *
import pytest

def test_first_chapter():
    obj = ParseMainPage('https://wikidth.net/truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co-Ya2smlS4CFNOCent#!')
    assert obj.get_first_chapter() == 'https://wikidth.net//truyen/xuyen-thu-tu-chan-gioi-vi-sao-nhu-the-co/chuong-1-chuong-1-Ya4AGsQsRA9yXFi1'