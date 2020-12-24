#!/usr/bin/env python
# coding: utf-8

from book import Book
from generallistedit import GeneralListEdit


class BookListEdit(GeneralListEdit):
    def new_rec(self, code=0, name='', img='', publ=None, year=0, pages=0):
        self.append_list(Book(code, name, img, publ, year, pages))

    def set_img(self, code, value):
        self.find_by_code(code).set_img(value)

    def set_publ(self, code, value):
        self.find_by_code(code).set_publ(value)

    def set_pages(self, code, value):
        self.find_by_code(code).set_pages(value)

    def set_year(self, code, value):
        self.find_by_code(code).set_year(value)

    def append_author(self, code, value):
        self.find_by_code(code).append_author(value)

    def remove_author(self, bcode, acode):
        self.find_by_code(bcode).remove_author(acode)

    def clear_authors(self, code):
        self.find_by_code(code).clear_authors()

    def get_img(self, code):
        return self.find_by_code(code).get_img()

    def get_publ_code(self, code):
        return self.find_by_code(code).get_publ_code()

    def get_publ_name(self, code):
        return self.find_by_code(code).get_publ_name()

    def get_publ_shortname(self, code):
        return self.find_by_code(code).get_publ_name()

    def get_pages(self, code):
        return self.find_by_code(code).get_pages()

    def get_year(self, code):
        return self.find_by_code(code).get_year()

    def get_author_surname(self, bcode, acode):
        return self.find_by_code(bcode).get_author_surname(acode)

    def get_author_name(self, bcode, acode):
        return self.find_by_code(bcode).get_author_name(acode)

    def get_author_secname(self, bcode, acode):
        return self.find_by_code(bcode).get_author_secname(acode)

    def get_author_shortname(self, bcode, acode):
        return self.find_by_code(bcode).get_author_shortname(acode)

    def get_author_shortsecname(self, bcode, acode):
        return self.find_by_code(bcode).get_author_shortsecname(acode)

    def get_author_codes(self, code):
        return self.find_by_code(code).get_author_codes()

    def get_authors_bibliostr(self, code):
        return self.find_by_code(code).get_authors_bibliostr()

    def get_bibliostr(self, code):
        return self.find_by_code(code).get_bibliostr()
