#!/usr/bin/env python
# coding: utf-8

from author import Author
from authorlist import AuthorList
from generallistedit import GeneralListEdit


class AuthorListEdit(AuthorList, GeneralListEdit):

    def new_rec(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        self.append_list(Author(code, surname, name, secname, shortname, shortsecname))

    def set_surname(self, code, value):
        self.find_by_code(code).set_surname(value)

    def set_name(self, code, value):
        self.find_by_code(code).set_name(value)

    def set_secname(self, code, value):
        self.find_by_code(code).set_secname(value)

    def set_shortname(self, code, value):
        self.find_by_code(code).set_shortname(value)

    def set_shortsecname(self, code, value):
        self.find_by_code(code).set_shortsecname(value)
