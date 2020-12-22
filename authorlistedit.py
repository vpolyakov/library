#!/usr/bin/env python
# coding: utf-8

from author import Author
from authorlist import AuthorList


class AuthorListEdit(AuthorList):
    # TODO

    def __init__(self):
        AuthorList.__init__(self)

    def new_author(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        self._authors.append(Author(code, surname, name, secname, shortname, shortsecname))

    def set_author_surname(self, code, value):
        self.findAuthorByCode(code).set_surname(value)

    def set_author_name(self, code, value):
        self.findAuthorByCode(code).set_name(value)

    def set_author_secname(self, code, value):
        self.findAuthorByCode(code).set_secname(value)

    def set_author_shortname(self, code, value):
        self.findAuthorByCode(code).set_shortname(value)

    def set_author_shortsecname(self, code, value):
        self.findAuthorByCode(code).set_shortsecname(value)
