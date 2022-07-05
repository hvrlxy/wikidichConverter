# wikidichConverter

This is a program to crawl book's content from [wikidich](wikidth.net] provided the link of the book, and convert all chapters into a pdf file.

## Download the package
Currently, the package is only available in TestPyPi. To download the package from the command line, use the command below:

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ wikidichConverter
```

## How to use it?

Currently, the package only support one function, converting the book url into a pdf file containing all the chapters. For example, to crawl all the content of [this](https://wikidth.net/truyen/su-tinh-nhung-dai-YhmIvTu2615a1j5G) book, we can use the convert_pdf() function, and provide the url of the book we want to crawl, and the path we want to store the pdf in.

```
from wikidichConverter.convert import *

convert_pdf('https://wikidth.net/truyen/su-tinh-nhung-dai-YhmIvTu2615a1j5G', 'new_book.pdf')
```

After running the code, a new pdf file called "new_book.pdf" will appear in your current directory.

To retrieve the book's name, we can utilize the get_book_name() function from the ParseMainPage() class:

```
from wikidichConverter.parse_mainpage import *

book_name = ParseMainPage('https://wikidth.net/truyen/su-tinh-nhung-dai-YhmIvTu2615a1j5G').get_book_name()
print(book_name)
```
