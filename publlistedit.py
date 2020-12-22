#!/usr/bin/env python
# coding: utf-8

from publ import Publ
from generallistedit import GeneralListEdit


class PublListEdit(GeneralListEdit):

    def new_rec(self, code=0, name='', shortname=''):
        self.append_list(Publ(code, name, shortname))

    def get_shortname(self, code):
        return self.find_by_code(code).get_shortname()

    def set_shortname(self, code, value):
        self.find_by_code(code).set_shortname(value)

# class PublListEdit:
#     def __init__(self):
#         self.__publs = []
#
#     def publ_clear(self):
#         self.__publs = []
#
#     def find_publ_by_code(self, code):
#         for p in self.__publs:
#             if p.get_code() == code:
#                 return p
#                 # break  ##
#
#     def append_publ(self, value=None):
#         self.__publs.append(value)
#
#     def remove_publ(self, code):
#         for s in self.__publs:
#             if s.get_code() == code:
#                 self.__publs.remove(s)
#
#     def get_publ_name(self, code):
#         return self.find_publ_by_code(code).get_name()
#
#     def get_publ_shortname(self, code):
#         return self.find_publ_by_code(code).get_shortname()
#
#     def new_publ(self, code=0, name='', shortname=''):
#         self.__publs.append(Publ(code, name, shortname))
#
#     def set_publ_name(self, code, value):
#         self.find_publ_by_code(code).set_name(value)
#
#     def set_publ_shortname(self, code, value):
#         self.find_publ_by_code(code).set_shortname(value)
#
#     def get_publ_list(self):
#         return [s.get_name() for s in self.__publs]
#
#     def get_publ_codes(self):
#         return [s.get_code() for s in self.__publs]
