#!/usr/bin/env python
# coding: utf-8

from general import General


class Publ(General):
    def __init__(self, code=0, name='', shortname=''):
        General.__init__(self, code, name)
        self.__shortname = None
        self.set_shortname(shortname)

    def set_shortname(self, value):
        self.__shortname = value

    def get_shortname(self):
        return self.__shortname
