#ex36 list1=[1,2,3,4...10]  print list1 reversed 

#ex1 การใช้ การ print กำหนด index
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[::-1])

#ex2  การใช้ append นำข้อมูลใส่ list ว่าง
list2=[]
for i in range(10,0,-1):
    list2.append(i)
print(list2)

#ex3 การใช้ metod ในการ จั
list3=[]
#input list
for i in range(1,10+1):
    list3.append(i)
#test input
print("list3=",list3)
# การเรียกใช้ metod sort และ reverse   เรียงข้อมมูลมาก ไป น้อย
list3.sort(reverse=True)
print(list3)