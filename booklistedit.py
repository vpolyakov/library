#!/usr/bin/env python
# coding: utf-8

# In[2]:


from book import book
class bookListEdit:
    def __init__(self):self.__books=[]
    def bookClear(self):self.__books=[]
    def findBookByCode(self,code):
        for b in self.__books:
            if b.getCode()==code:
                return b
                break 
    def appendBook(self,value=None):self.__books.append(value)
    def removeBook(self,code):
        for s in self.__books:
            if s.getcode()==code:self.__books.remove(s)
    def newBook(self,code=0,name='',publ=None,year=0,pages=0):
        self.__books.append(book(code,name,publ,year,pages))
    def setBookName(self,code,value):self.findBookByCode(code).setName(value)    
    def setBookPubl(self,code,value):self.findBookByCode(code).setPubl(value)
    def setBookPages(self,code,value):self.findBookByCode(code).setPages(value)
    def setBookYear(self,code,value):self.findBookByCode(code).setYear(value)
    def appendBookAuthor(self,code,value):self.findBookByCode(code).appendAuthor(value)
    def removeBookAuthor(self,bcode,acode):self.findBookByCode(code).removeAuthor(acode)
    def getBookName(self,code):return self.findBookByCode(code).getName()
    def getBookPublCode(self,code):return self.findBookByCode(code).getPublCode()
    def getBookPublName(self,code):return self.findBookByCode(code).getPublName()
    def getBookPublShortname(self,code):return self.findBookByCode(code).getPublName()
    def getBookPages(self,code):return self.findBookByCode(code).getPages()
    def getBookYear(self,code):return self.findBookByCode(code).getYear()
    def getBookAuthorsForBibliostr(self,code):return self.findBookByCode(code).getAuthorsForBibliostr()
    def getBookAuthorSurname(self,bcode,acode):return self.findBookByCode(code).getAuthorSurname(acode)
    def getBookAuthorName(self,bcode,acode):return self.findBookByCode(code).getAuthorName(acode)
    def getBookAuthorSecname(self,bcode,acode):return self.findBookByCode(code).getAuthorSecname(acode)
    def getBookAuthorShortname(self,bcode,acode):return self.findBookByCode(code).getAuthorShortname(acode)
    def getBookAuthorShortsecname(self,bcode,acode):return self.findBookByCode(code).getAuthorShortsecname(acode)
    def getBookBibliostr(self,code):return self.findBookByCode(code).getBibliostr()
    def getBookCodes(self):return [s.getCode() for s in self.__books]
    def getBibliostrs(self):return [s.getBibliostr() for s in self.__books]
    def getBookAuthorCodes(self,code):return self.findBookByCode(code).getAuthorCodes()

