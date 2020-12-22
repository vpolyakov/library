# -*- coding:utf-8 -*-

from author import Author
from book import Book
from publ import Publ

b1 = Book(1, 'Матричный анализ', 'matrix.jpeg', year=1989, pages=655)
b1.append_author(Author(1, 'Хорн', 'Роджер', shortname='Р'))
b1.append_author(Author(2, 'Джонсон', 'Чарльз', shortname='Ч'))
b1.set_publ(Publ(1, 'Москва "Мир"', 'М.: Мир'))
print(b1.get_bibliostr())
