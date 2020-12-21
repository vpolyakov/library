#!/usr/bin/env python
# coding: utf-8

# In[5]:


from general import general
from publ import publ
from authorlist import authorList
class book(general):
    def __init__(self,code=0,name='',img='',publ=None,year=0,pages=0):
        general.__init__(self,code,name)
        self.__authors=authorList()
        self.setImg(img)
        self.setPubl(publ)
        self.setPages(pages)
        self.setYear(year)
    def setImg(self,value):self.__img=value
    def setPubl(self,value):
        if isinstance(value,publ):self.__publ=value
    def setPages(self,value):self.__pages=value
    def setYear(self,value):self.__year=value
    def getImg(self):return self.__img
    def getPublCode(self):
        if self.__publ:return self.__publ.getCode()
    def getPublName(self):
        if self.__publ:return self.__publ.getName()
        else:return ''
    def getPublShortname(self):
        if self.__publ:return self.__publ.getShortname()
        else:return ''
    def getPages(self):return self.__pages
    def getYear(self):return self.__year
    def appendAuthor(self,value):self.__authors.appendList(value)
    def removeAuthor(self,code):self.__authors.removeList(code)
    def clearAuthors(self):self.__authors.clear()
    def getAuthorCodes(self):return self.__authors.getCodes()
    def getAuthorName(self,code):return self.__authors.findByCode(code).getSurname()
    def getAuthorSurname(self,code):return self.__authors.findByCode(code).getSurname()
    def getAuthorSecname(self,code):return self.__authors.findByCode(code).getSecname()
    def getAuthorShortname(self,code):return self.__authors.findByCode(code).getShortname()
    def getAuthorShortsecname(self,code):return self.__authors.findByCode(code).getShortsecname()
    def getAuthorsBibliostr(self):return self.__authors.getListBibliostr()
    def getBibliostr(self):
        s=self.getAuthorsBibliostr()
        s+=' %s - %s, %s. - %s c.'%(self.getName(),self.getPublShortname(),str(self.getYear()),str(self.getPages()))
        return s


# In[ ]:




