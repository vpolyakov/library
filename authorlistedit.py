#!/usr/bin/env python
# coding: utf-8

from authorlist import authorList
from author import author


class authorListEdit(authorList):
    def __init__(self):
        authorList.__init__(self)

    def newAuthor(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        self._authors.append(author(code, surname, name, secname, shortname, shortsecname))

    def setAuthorSurname(self, code, value):
        self.findAuthorByCode(code).setSurname(value)

    def setAuthorName(self, code, value):
        self.findAuthorByCode(code).setName(value)

    def setAuthorSecname(self, code, value):
        self.findAuthorByCode(code).setSecname(value)

    def setAuthorShortname(self, code, value):
        self.findAuthorByCode(code).setShortname(value)

    def setAuthorShortsecname(self, code, value):
        self.findAuthorByCode(code).setShortsecname(value)
