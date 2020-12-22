#!/usr/bin/env python
# coding: utf-8

class GeneralList:
    def __init__(self):
        self.__list = []

    def clear(self):
        self.__list = []

    def find_by_code(self, code):
        for item in self.__list:  # Добавил Изменил l на item
            if item.get_code() == code:
                return item

    def get_codes(self):
        return [s.get_code() for s in self.__list]

    def append_list(self, value):
        self.__list.append(value)

    def remove_list(self, code):
        for s in self.__list:
            if s.get_code() == code:
                self.__list.remove(s)

    def get_name(self, code):
        return self.find_by_code(code).get_name()
