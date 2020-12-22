#!/usr/bin/env python
# coding: utf-8


class Data:
    def __init__(self, lib=None, inp='', out=''):
        self.__lib = None
        self.__inp = None
        self.__out = None
        self.set_lib(lib)
        self.set_inp(inp)
        self.set_out(out)

    def set_lib(self, value):
        self.__lib = value

    def set_inp(self, value):
        self.__inp = value

    def set_out(self, value):
        self.__out = value

    def get_lib(self):
        return self.__lib

    def get_inp(self):
        return self.__inp

    def get_out(self):
        return self.__out

    def read_file(self, filename):
        self.set_inp(filename)
        self.read()

    def write_file(self, filename):
        self.set_out(filename)
        self.write()

    # TODO
    def read(self):
        pass

    def write(self):
        pass
