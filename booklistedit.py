#!/usr/bin/env python
# coding: utf-8

from book import Book


class BookListEdit:
    def __init__(self):
        self.__books = []

    def book_clear(self):
        self.__books = []

    def find_book_by_code(self, code):
        for b in self.__books:
            if b.get_code() == code:
                return b
                # break   # Добавил

    def append_book(self, value=None):
        self.__books.append(value)

    def remove_book(self, code):
        for s in self.__books:
            if s.getcode() == code:
                self.__books.remove(s)

    def new_book(self, code=0, name='', publ=None, year=0, pages=0):  # Пример
        self.__books.append(Book(code, name, publ, year, pages))

    def set_book_name(self, code, value):
        self.find_book_by_code(code).set_name(value)

    def set_book_publ(self, code, value):
        self.find_book_by_code(code).set_publ(value)

    def set_book_pages(self, code, value):
        self.find_book_by_code(code).set_pages(value)

    def set_book_year(self, code, value):
        self.find_book_by_code(code).set_year(value)

    def append_book_author(self, code, value):
        self.find_book_by_code(code).append_author(value)

    def remove_book_author(self, bcode, acode):
        self.find_book_by_code(bcode).remove_author(acode)

    def get_book_name(self, code):
        return self.find_book_by_code(code).get_name()

    def get_book_publ_code(self, code):
        return self.find_book_by_code(code).get_publ_code()

    def get_book_publ_name(self, code):
        return self.find_book_by_code(code).get_publ_name()

    def get_book_publ_shortname(self, code):
        return self.find_book_by_code(code).get_publ_name()

    def get_book_pages(self, code):
        return self.find_book_by_code(code).get_pages()

    def get_book_year(self, code):
        return self.find_book_by_code(code).get_year()

    def get_book_authors_for_bibliostr(self, code):
        return self.find_book_by_code(code).getAuthorsForBibliostr()

    def get_book_author_surname(self, bcode, acode):  # Добавил всесто code bcode
        return self.find_book_by_code(bcode).get_author_surname(acode)

    def get_book_author_name(self, bcode, acode):
        return self.find_book_by_code(bcode).get_author_name(acode)  # Добавил всесто code bcode

    def get_book_author_secname(self, bcode, acode):
        return self.find_book_by_code(bcode).get_author_secname(acode)  # Добавил всесто code bcode

    def get_book_author_shortname(self, bcode, acode):  # Добавил всесто code bcode
        return self.find_book_by_code(bcode).get_author_shortname(acode)

    def get_book_author_shortsecname(self, bcode, acode):
        return self.find_book_by_code(bcode).get_author_shortsecname(acode)  # Добавил всесто code bcode

    def get_book_bibliostr(self, code):
        return self.find_book_by_code(code).get_bibliostr()

    def get_book_codes(self):
        return [s.get_code() for s in self.__books]

    def get_bibliostrs(self):
        return [s.get_bibliostr() for s in self.__books]

    def get_book_author_codes(self, code):
        return self.find_book_by_code(code).get_author_codes()
