#!/usr/bin/env python
# coding: utf-8

from generallist import GeneralList


class GeneralListEdit(GeneralList):
    def get_new_code(self):
        m = 0
        for c in self.get_codes():
            if c > m:
                m = c
        return m + 1

    def set_name(self, code, value):
        self.find_by_code(code).set_name(value)
