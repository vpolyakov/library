#!/usr/bin/env python
# coding: utf-8

from general import general


class author(general):
    def __init__(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        general.__init__(self, code, name)
        self.setSurname(surname)
        self.setSecname(secname)
        self.setShortname(shortname)
        self.setShortsecname(shortsecname)

    def setSurname(self, value):
        self.__surname = value

    def setSecname(self, value):
        self.__secname = value

    def setShortname(self, value):
        self.__shortname=value

    def setShortsecname(self, value):
        self.__shortsecname = value

    def getSurname(self):
        return self.__surname

    def getSecname(self):
        return self.__secname

    def getShortname(self):
        return self.__shortname

    def getShortsecname(self):
        return self.__shortsecname

    def getBibliostr(self):
        s = self.getSurname()
        if self.getShortname():
            s += ' %s.' % (self.getShortname(),)
        if self.getShortsecname():
            s += ' %s.' % (self.getShortsecname(),)
        return s
