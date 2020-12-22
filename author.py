#!/usr/bin/env python
# coding: utf-8

from general import General


class Author(General):
    def __init__(self, code=0, surname='', name='', secname='', shortname='', shortsecname=''):
        General.__init__(self, code, name)
        self.__surname = None
        self.__secname = None
        self.__shortname = None
        self.__shortsecname = None
        self.set_surname(surname)
        self.set_secname(secname)
        self.set_shortname(shortname)
        self.set_shortsecname(shortsecname)

    def set_surname(self, value):
        self.__surname = value

    def set_secname(self, value):
        self.__secname = value

    def set_shortname(self, value):
        self.__shortname = value

    def set_shortsecname(self, value):
        self.__shortsecname = value

    def get_surname(self):
        return self.__surname

    def get_secname(self):
        return self.__secname

    def get_shortname(self):
        return self.__shortname

    def get_shortsecname(self):
        return self.__shortsecname

    def get_bibliostr(self):
        s = self.get_surname()
        if self.get_shortname():
            s += ' %s.' % (self.get_shortname(),)
        if self.get_shortsecname():
            s += ' %s.' % (self.get_shortsecname(),)
        return s
