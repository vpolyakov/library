#!/usr/bin/env python
# coding: utf-8

# In[2]:


from generallist import generalList
class generalListEdit(generalList):
    def getNewCode(self):
        m=0
        for c in self.getCodes():
            if c>m:m=c
        return m+1
    def setName(self,code,value):self.findByCode(code).setName(value)


# In[ ]:




