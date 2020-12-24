#!/usr/bin/env python
# coding: utf-8

from authorlist import AuthorList
from general import General
from publ import Publ


class Book(General):
    def __init__(self, code=0, name='', img='', publ=None, year=0, pages=0):
        General.__init__(self, code, name)
        self.__img = None
        self.__publ = None
        self.__pages = None
        self.__year = None
        self.__authors = AuthorList()
        self.set_img(img)
        self.set_publ(publ)
        self.set_pages(pages)
        self.set_year(year)

    def set_img(self, value):
        self.__img = value

    def set_publ(self, value):
        if isinstance(value, Publ):
            self.__publ = value

    def set_pages(self, value):
        self.__pages = value

    def set_year(self, value):
        self.__year = value

    def get_img(self):
        return self.__img

    def get_publ_code(self):
        if self.__publ:
            return self.__publ.get_code()

    def get_publ_name(self):
        if self.__publ:
            return self.__publ.get_name()
        else:
            return ''

    def get_publ_shortname(self):
        if self.__publ:
            return self.__publ.get_shortname()
        else:
            return ''

    def get_pages(self):
        return self.__pages

    def get_year(self):
        return self.__year

    def append_author(self, value):
        self.__authors.append_list(value)

    def remove_author(self, code):
        self.__authors.remove_list(code)

    def clear_authors(self):
        self.__authors.clear()

    def get_author_codes(self):
        return self.__authors.get_codes()

    def get_author_name(self, code):
        return self.__authors.find_by_code(code).get_name()

    def get_author_surname(self, code):
        return self.__authors.find_by_code(code).get_surname()

    def get_author_secname(self, code):
        return self.__authors.find_by_code(code).get_secname()

    def get_author_shortname(self, code):
        return self.__authors.find_by_code(code).get_shortname()

    def get_author_shortsecname(self, code):
        return self.__authors.find_by_code(code).get_shortsecname()

    def get_authors_bibliostr(self):
        return self.__authors.get_list_bibliostr()

    def get_bibliostr(self):
        s = self.get_authors_bibliostr()
        s += ' %s - %s, %s. - %s c.' % (self.get_name(), self.get_publ_shortname(),
                                        str(self.get_year()), str(self.get_pages()))
        return s
