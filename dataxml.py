#!/usr/bin/env python
# coding: utf-8

import xml.dom.minidom


class DataXML:
    @staticmethod
    def read(inp, lib):
        dom = xml.dom.minidom.parse(inp)
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'author'):
                code, surname, name, secname, shortname, shortsecname = 0, "", "", "", "", ""
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "surname":
                        surname = t[1]
                    if t[0] == "secname":
                        secname = t[1]
                    if t[0] == "shortname":
                        shortname = t[1]
                    if t[0] == "shortsecname":
                        shortsecname = t[1]
                lib.new_author(code, surname, name, secname, shortname, shortsecname)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'publ'):
                code, name, shortname = 0, "", ""
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "shortname":
                        shortname = t[1]
                lib.new_publ(code, name, shortname)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'book'):
                code, name, publ, year, pages = 0, '', None, 0, 0
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "year":
                        year = int(t[1])
                    if t[0] == "pages":
                        pages = int(t[1])
                    if t[0] == "publ":
                        publ = lib.find_publ_by_code(int(t[1]))
                lib.new_book(code, name, publ, year, pages)
                for n in node.childNodes:
                    if (n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'author'):
                        for t in n.attributes.items():
                            if t[0] == "code":
                                author = lib.find_author_by_code(int(t[1]))
                lib.append_book_author(code, author)

    @staticmethod
    def write(out, lib):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("library")
        dom.appendChild(root)
        for c in lib.get_author_codes():
            aut = dom.createElement("author")
            aut.setAttribute('code', str(c))
            aut.setAttribute('surname', lib.get_author_surname(c))
            aut.setAttribute('name', lib.get_author_name(c))
            aut.setAttribute('secname', lib.get_author_secname(c))
            aut.setAttribute('shortname', lib.get_author_shortname(c))
            aut.setAttribute('shortsecname', lib.get_author_shortsecname(c))
            root.appendChild(aut)
        for c in lib.get_publ_codes():
            pub = dom.createElement("publ")
            pub.setAttribute('code', str(c))
            pub.setAttribute('name', lib.get_publ_name(c))
            pub.setAttribute('shortname', lib.get_publ_shortname(c))
            root.appendChild(pub)
        for c in lib.get_book_codes():
            bk = dom.createElement("book")
            bk.setAttribute('code', str(c))
            bk.setAttribute('name', lib.get_book_name(c))
            bk.setAttribute('year', str(lib.get_book_year(c)))
            bk.setAttribute('pages', str(lib.get_book_pages(c)))
            bk.setAttribute('publ', str(lib.get_book_publ_code(c)))
        for ac in lib.get_book_author_codes(c):
            aut = dom.createElement("author")
            aut.setAttribute('code', str(ac))
            bk.appendChild(aut)
            root.appendChild(bk)
            f = open(out, "wb")
            f.write(dom.toprettyxml(encoding='utf-8'))
            f.close()
