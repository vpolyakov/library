#!/usr/bin/env python
# coding: utf-8

# import os
import xml.dom.minidom


class dataxml:
    def read(self, inp, lib):
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
                lib.newAuthor(code, surname, name, secname, shortname, shortsecname)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'publ'):
                code, name, shortname = 0, "", ""
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "shortname":
                        shortname = t[1]
                lib.newPubl(code, name, shortname)
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
                        publ = lib.findPublByCode(int(t[1]))
                lib.newBook(code, name, publ, year, pages)
                for n in node.childNodes:
                    if (n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'author'):
                        for t in n.attributes.items():
                            if t[0] == "code":
                                author = lib.findAuthorByCode(int(t[1]))
                lib.appendBookAuthor(code, author)

    # def write(self, out, lib):
    #     dom = xml.dom.minidom.Document()
    #     oot = dom.createElement("library")
    #     dom.appendChild(root)
    #     for c in lib.getAuthorCodes():
    #         aut = dom.createElement("author")
    #         aut.setAttribute('code', str(c))
    #         aut.setAttribute('surname', lib.getAuthorSurname(c))
    #         aut.setAttribute('name', lib.getAuthorName(c))
    #         aut.setAttribute('secname', lib.getAuthorSecname(c))
    #         aut.setAttribute('shortname', lib.getAuthorShortname(c))
    #         aut.setAttribute('shortsecname', lib.getAuthorShortsecname(c))
    #         root.appendChild(aut)
    #     for c in lib.getPublCodes():
    #         pub = dom.createElement("publ")
    #         pub.setAttribute('code', str(c))
    #         pub.setAttribute('name', lib.getPublName(c))
    #         pub.setAttribute('shortname', lib.getPublShortname(c))
    #         root.appendChild(pub)
    #     for c in lib.getBookCodes():
    #         bk = dom.createElement("book")
    #         bk.setAttribute('code', str(c))
    #         bk.setAttribute('name', lib.getBookName(c))
    #         bk.setAttribute('year', str(lib.getBookYear(c)))
    #         bk.setAttribute('pages', str(lib.getBookPages(c)))
    #         bk.setAttribute('publ', str(lib.getBookPublCode(c)))
    #     for ac in lib.getBookAuthorCodes(c):
    #         aut = dom.createElement("author")
    #         aut.setAttribute('code', str(ac))
    #         bk.appendChild(aut)
    #         root.appendChild(bk)
    #         f = open(out, "w")
    #         f.write(dom.toprettyxml(encoding='utf-8'))
