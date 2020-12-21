#!/usr/bin/env python
# coding: utf-8

from authorlistedit import authorListEdit
from publlistedit import publListEdit
from booklistedit import bookListEdit


class library(authorListEdit, publListEdit, bookListEdit):
    def __init__(self):
        authorListEdit.__init__(self)
        publListEdit.__init__(self)
        bookListEdit.__init__(self)

    def removeauthor(self, code):
        authorListEdit.removeAuthor(self, code)
        for c in self.getBookCodes():
            self.removeBookAuthor(c, code)

    def removepubl(self, code):
        publListEdit.removePubl(self, code)
        for c in self.getBookCodes():
            self.setBookPubl(c, None)

    def clear(self):
        self.bookClear()
        self.authorClear()
        self.publClear()
