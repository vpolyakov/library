#!/usr/bin/env python
# coding: utf-8


class Data:
    def __init__(self, lib=None, inp='', out=''):
        self.setLib(lib)
        self.setInp(inp)
        self.setOut(out)

    def setLib(self, value):
        self.__lib = value

    def setInp(self, value):
        self.__inp = value

    def setOut(self, value):
        self.__out = value

    def getLib(self):
        return self.__lib

    def getInp(self):
        return self.__inp

    def getOut(self):
        return self.__out

    def readFile(self, filename):
        self.setInp(filename)
        self.read()

    def writeFile(self, filename):
        self.setOut(filename)
        self.write()

    def read(self):
        pass

    def write(self):
        pass
