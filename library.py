#!/usr/bin/env python
# coding: utf-8

from authorlistedit import AuthorListEdit
from booklistedit import BookListEdit
from publlistedit import PublListEdit


class Library:
    def __init__(self):
        self.__authors = AuthorListEdit()
        self.__publs = PublListEdit()
        self.__books = BookListEdit()

    def remove_author(self, code):
        self.__authors.remove_list(code)
        for c in self.__books.get_codes()():
            self.__books.remove_author(c, code)

    def remove_publ(self, code):
        self.__publs.remove_list(code)
        for c in self.__books.get_codes():
            self.__books.set_publ(c, None)

    def clear(self):
        self.__books.clear()
        self.__authors.clear()
        self.__publs.clear()

    def new_author(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        self.__authors.new_rec(code, surname, name, secname, shortname, shortsecname)

    def find_author_by_code(self, code):
        return self.__authors.find_by_code(code)

    def get_author_new_code(self):
        return self.__authors.get_new_code()

    def get_author_codes(self):
        return self.__authors.get_codes()

    def get_author_name(self, code):
        return self.__authors.get_name(code)

    def get_author_surname(self, code):
        return self.__authors.get_surname(code)

    def get_author_secname(self, code):
        return self.__authors.get_secname(code)

    def get_author_shortname(self, code):
        return self.__authors.get_shortname(code)

    def get_author_shortsecname(self, code):
        return self.__authors.get_shortsecname(code)

    def get_author_bibliostr(self, code):
        return self.__authors.get_bibliostr(code)

    def set_author_name(self, code, value):
        self.__authors.set_name(code, value)

    def set_author_surname(self, code, value):
        self.__authors.set_surname(code, value)

    def set_author_secname(self, code, value):
        self.__authors.set_secname(code, value)

    def set_author_shortname(self, code, value):
        self.__authors.set_shortname(code, value)

    def set_author_shortsecname(self, code, value):
        self.__authors.set_shortsecname(code, value)

    def new_publ(self, code=0, name='', shortname=''):
        self.__publs.new_rec(code, name, shortname)

    def find_publ_by_code(self, code):
        return self.__publs.find_by_code(code)

    def get_publ_codes(self):
        return self.__publs.get_codes()

    def get_publ_name(self, code):
        return self.__publs.get_name(code)

    def get_publ_shortname(self, code):
        return self.__publs.get_shortname(code)

    def get_publ_new_code(self):
        return self.__publs.get_new_code()

    def set_publ_name(self, code, value):
        self.__publs.set_name(code, value)

    def set_publ_shortname(self, code, value):
        self.__publs.set_shortname(code, value)

    def remove_book(self, code):
        self.__books.remove_list(code)

    def new_book(self, code=0, name='', img='', publ=None, year=0, pages=0):
        self.__books.new_rec(code, name, img, publ, year, pages)

    def find_book_by_code(self, code):
        return self.__books.find_by_code(code)

    def append_book_author(self, bcode, value):
        self.__books.append_author(bcode, value)

    def remove_book_author(self, bcode, acode):
        self.__books.remove_author(bcode, acode)

    def clear_book_authors(self, bcode):
        self.__books.clear_authors(bcode)

    def set_book_name(self, code, value):
        self.__books.set_name(code, value)

    def set_book_img(self, code, value):
        self.__books.set_img(code, value)

    def set_book_publ(self, code, pcode):
        self.__books.set_publ(code, self.find_publ_by_code(pcode))

    def set_book_pages(self, code, value):
        self.__books.set_pages(code, value)

    def set_book_year(self, code, value):
        self.__books.set_year(code, value)

    def get_book_codes(self):
        return self.__books.get_codes()

    def get_book_new_code(self):
        return self.__books.get_new_code()

    def get_book_name(self, code):
        return self.__books.get_name(code)

    def get_book_img(self, code):
        return self.__books.get_img(code)

    def get_book_publ_code(self, code):
        return self.__books.get_publ_code(code)

    def get_book_publ_name(self, code):
        return self.__books.get_pub_name(code)

    def get_book_publ_shortname(self, code):
        return self.__books.get_pub_name(code)

    def get_book_pages(self, code):
        return self.__books.get_pages(code)

    def get_book_year(self, code):
        return self.__books.get_year(code)

    def get_book_author_surname(self, bcode, acode):
        return self.__books.get_author_surname(bcode, acode)

    def get_book_author_name(self, bcode, acode):
        return self.__books.get_author_name(bcode, acode)

    def get_book_author_secname(self, bcode, acode):
        return self.__books.get_author_secname(bcode, acode)

    def get_book_author_shortname(self, bcode, acode):
        return self.__books.get_author_shortname(bcode, acode)

    def get_book_author_shortsecname(self, bcode, acode):
        return self.__books.get_author_shortsecname(bcode, acode)

    def get_book_author_codes(self, code):
        return self.__books.get_author_codes(code)

    def get_book_authors_bibliostr(self, code):
        return self.__books.get_authors_bibliostr(code)

    def get_book_bibliostr(self, code):
        return self.__books.get_bibliostr(code)

    def get_bibliostr(self):
        __bibliostr = []
        for code in self.get_book_codes():
            __bibliostr.append(self.get_book_bibliostr(code))
        return __bibliostr
