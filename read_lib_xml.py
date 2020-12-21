from library import library
from dataxml import dataxml as data_lib

lib1 = library()
dat1 = data_lib()

dat1.read('my_lib.xml', lib1)
