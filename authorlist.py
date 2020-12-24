#!/usr/bin/env python
# coding: utf-8

from generallist import GeneralList


class AuthorList(GeneralList):
    def get_surname(self, code):
        return self.find_by_code(code).get_surname()

    def get_secname(self, code):
        return self.find_by_code(code).get_secname()

    def get_shortname(self, code):
        return self.find_by_code(code).get_shortname()

    def get_shortsecname(self, code):
        return self.find_by_code(code).get_shortsecname()

    def get_bibliostr(self, code):
        return self.find_by_code(code).get_bibliostr()

    def get_list_bibliostr(self):
        s = ''
        for code in self.get_codes():
            s += self.get_bibliostr(code) + ', '
        if s:
            s = s[:-2]
        return s
