#!/usr/bin/env python
# coding: utf-8

from authorlistedit import AuthorListEdit
from booklistedit import BookListEdit
from publlistedit import PublListEdit


class Library(AuthorListEdit, PublListEdit, BookListEdit):
    def __init__(self):
        AuthorListEdit.__init__(self)
        PublListEdit.__init__(self)
        BookListEdit.__init__(self)

    def removeauthor(self, code):
        AuthorListEdit.removeAuthor(self, code)
        for c in self.get_book_codes():
            self.remove_book_author(c, code)

    def removepubl(self, code):
        PublListEdit.remove_publ(self, code)
        for c in self.get_book_codes():
            self.set_book_publ(c, None)

    def clear(self):
        self.book_clear()
        self.authorClear()
        self.publ_clear()
