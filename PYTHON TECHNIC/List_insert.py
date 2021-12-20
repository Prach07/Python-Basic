#44 listx=[0,2,4,6,8] และ list4=['a','b','c','d','e','f'] เขียนโปรแกรม แทรก(insert) '*' in list4 ใน index listx
# list.insert(index, item)  <-pattern
listx=[0,2,4,6,8]
list4=['a','b','c','d','e','f']

for i in range(len(listx)):
    list4.insert(listx[i],'*')#insert listx[i] ด้วย '*' ใส่ไว้ใน list4
print(list4)