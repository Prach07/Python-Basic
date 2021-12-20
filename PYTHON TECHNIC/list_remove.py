#ex48 list4=['a','b','c','d','e','f']  input str1 . check str1 in list4 Y remove() str1 in list1  N do not thing

list4=['a','b','c','d','e','f']
str1=input("Enter char:")
if str1 in list4:
    list4.remove(str1)
else:
    pass
print(list4)