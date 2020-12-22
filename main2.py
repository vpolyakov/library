from library import Library
from dataxml import DataXML

lib1 = Library()
dat1 = DataXML()
dat1.read('my_lib.xml', lib1)

dat1.write('new.xml', lib1)

print(lib1.get_book_bibliostr(1))
print(lib1.get_author_codes())
