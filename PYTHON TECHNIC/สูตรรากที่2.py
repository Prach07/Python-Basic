#ex43 list3=[1,2,3,..25]  เปลี่ยนสมาชิกใน list3ที่ ถอดรากที่สอง แล้วเป็นจำนวนเต็ม  ให้เป็น 'square' print list3
#input list3 to number 1-25
import math

list3=[]
for i in range(1,26):
     list3.append(i)
#check list3
print(list3)

#print ถอดรากที่สอง แล้วเป็นจำนวนเต็ม  ให้เป็น 'square'
for i in range(len(list3)):
    if (list3[i]**(1/2))%1 ==0: #สูตร หารากที่สอง  example 16(4) ,4(2) 2 เป็นรากที่ 2ของ 4
        list3[i]='square'

#print result
print(list3)