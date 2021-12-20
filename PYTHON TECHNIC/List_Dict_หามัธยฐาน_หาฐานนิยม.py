#ฐานนิยม 
'''

#99  input 5 int  หาฐานนิยม และพิมม์ออกมา สูตร มัยธฐาน  N +1 / 2  เมื่อ  คือ จำนวนของข้อมูล 

#logic 1. input 5 integer by loop  2. หาฐานนิยม

list1=[]
for i in range(5):
    number=int(input())
    list1.append(number)
    
set1=set(list1) # cast list to set
dict1={}   
for x in set1:
    n =list1.count(x) # นับ สมาชิก x  in set1   ตามจำนวนครั้งที่ปรากฏ
    dict1[x] =n # dict1 key x  ไล่ลำดับ เก็บ value  n 
isFirstEle=True
for x in dict1:
    if isFirstEle == True:
        count_max = dict1[x]
        mode = x 
        isFirstEle = False
    else:
        if dict1[x] > count_max:
            count_max =dict1[x]
            mode=x 
print(mode)
'''
# มัธยฐาน  median 
'''

#94 list1=[1,3,7,9,2,7,5,1,8]  หา มัธยฐาน(ค่ากึงกลางของข้อมูล) ของ ข้อมูลใน list1 
#สูตร มัยธฐาน  N +1 / 2  เมื่อ  คือ จำนวนของข้อมูล 

list1=[1,3,7,9,2,7,5,1,8]
sorted_list1=sorted(list1) # เรียงข้อมูลจากน้อยไปมาก  ถ้ามากไปน้อย ก็ reverse อีกที
n= len(sorted_list1) # ความยาว ข้อมูล list1 

if n%2 ==1: # ถ้า n เป็นเลขคี่ 
    pos = int((n-1)/2)  # สร้างตัวแปร ชื่อ pos เพื่อคำนวนค่ากลางของ n ในรูปแบบจำนวนเต็ม 
    median=sorted_list1[pos] # สร้างตัวแปรชื่อ median กำหนดค่าเท่ากับ สมาชิกของ sorted_list1 ตำแหน่งที่ pos
else:
    pos = int(n/2) # ถ้า n เป็นเลขคู่ 
    median=(sorted_list1[pos-1]+sorted_list1[pos])/2

print(median) 

'''
#หา มัธยฐาน แบบ ข้อมูล ใน dictionary 
'''
#96 data={'Brazil':35000,'China':24000,'Germany':42000,'Japan':53000,'Sweden':17000} 
#หา มัธยฐาน ใน data

#data
data={'Brazil':35000,'China':24000,'Germany':42000,'Japan':53000,'Sweden':17000} 
#เรียงข้อมูลก่อน 
sorted_data=sorted(data)
#check data sorted
print(sorted_data)
n=len(sorted_data)
if n%2 ==1: # ถ้า n เป็นเลขคี่ 
    pos = int((n-1)/2)  # สร้างตัวแปร ชื่อ pos เพื่อคำนวนค่ากลางของ n ในรูปแบบจำนวนเต็ม 
    median=sorted_data[pos] # สร้างตัวแปรชื่อ median กำหนดค่าเท่ากับ สมาชิกของ sorted_list1 ตำแหน่งที่ pos
else:
    pos = int(n/2) # ถ้า n เป็นเลขคู่ 
    median=(sorted_data[pos-1]+sorted_data[pos])/2

print(median)
 '''
