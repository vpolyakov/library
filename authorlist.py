#!/usr/bin/env python
# coding: utf-8

from generallist import generalList


class authorList(generalList):
    def getSurname(self, code):
        return self.findByCode(code).getSurname()

    def getSecname(self, code):
        return self.findByCode(code).getSecname()

    def getShortname(self, code):
        return self.findByCode(code).getShortname()

    def getShortsecname(self, code):
        return self.findByCode(code).getShortsecname()

    def getBibliostr(self, code):
        return self.findByCode(code).getBibliostr()

    def getListBibliostr(self):
        s = ''
        for code in self.getCodes():
            s += self.getBibliostr(code)+', '
            if s:
                s = s[:-2]
            return s
