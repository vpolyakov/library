#!/usr/bin/env python
# coding: utf-8

# In[1]:


from general import general
class publ(general):
    def __init__(self,code=0,name='',shortname=''):
        general.__init__(self,code,name)
        self.setShortname(shortname)
    def setShortname(self,value):self.__shortname=value
    def getShortname(self):return self.__shortname


# In[ ]:






