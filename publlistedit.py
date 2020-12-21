#!/usr/bin/env python
# coding: utf-8

# In[2]:


from publ import publ

class publListEdit:
    def __init__(self):self.__publs=[]
    def publClear(self):self.__publs=[]
    def findPublByCode(self,code):
        for p in self.__publs:
            if p.getCode()==code:
                return p
                break
    def appendPubl(self,value=None):self.__publs.append(value)   
    def removePubl(self,code):    
        for s in self.__publs:    
            if s.getCode()==code:self.__publs.remove(s)
    def getPublName(self,code):return self.findPublByCode(code).getName()                                                   
    def getPublShortname(self,code):return self.findPublByCode(code).getShortname()
    def newPubl(self,code=0,name='',shortname=''):self.__publs.append(publ(code,name,shortname))
    def setPublName(self,code,value):self.findPublByCode(code).setName(value)
    def setPublShortname(self,code,value):self.findPublByCode(code).setShortname(value)
    def getPublList(self):return [s.getName() for s in self.__publs]
    def getPublCodes(self):return [s.getCode() for s in self.__publs]  

