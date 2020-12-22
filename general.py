#!/usr/bin/env python
# coding: utf-8

class General:
    def __init__(self, code=0, name=''):
        self.__code = None  # Добавил
        self.__name = None  # Добавил
        self.set_code(code)
        self.set_name(name)

    def set_code(self, value):
        self.__code = value

    def set_name(self, value):
        self.__name = value

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name
