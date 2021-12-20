#101 programs print x    10 Col  10 low
'''
for i in range(10):
    for j in range(10):  #Coulume 
        print('x',end="") 
    print() # ขึ้นบรรทัดใหม่ 
'''

#102   col 1 + ... 10  low10   
# x
#xx
#xxx
#logic     loop แรกมากำหนด Print กี่รรทัด 
'''
for i in range(10): # low
    for j in range(i+1):  # Col เริ่มจาก 0 บวกไปที่ละ ค่าของ i 
        print('x',end="") # print ต่อกัน
    print() #บรรทัดใหม่ 
'''

#103  col 10 .. 1   low 10 
# xxx
#xx
#x
# logic  i  กำหนด การ print 
''''
for i in range(9,-1,-1): #low 10
    for j in range(i+1):  #Col   รอบแรกเป็น 9+1   print x , รอบสองเป็น 8+1 print x .......
        print('x',end='') 
    print()
'''

#104   
'''
---x
--xxx
-xxxxx
xxxxxxx
'''
#logic    x 1+2   - 3-1   loop print -  , loop print x 
'''
for i in range(4):
    for j in range(4+i): #j=0 -> j<3-0 print -  , else print x  ->>> j=1->j<3-1 print - , else print x
        if j <3-i:
            print('-',end='')
        else:
            print('x',end='')
    print() '''
    
#104  ex2
'''
---x
--xxx
-xxxxx
xxxxxxx
'''
#logic  low4   colume std 4   +1 
'''
for i in range(4):  
    for j in range(4+i):   #เพิ่มจำนวน colum ตาม ค่า  i    ค่า j เพิ่มค่า ทุกรอบ 
        # print -  and x   หมายถึงมี 2 เงื่อนไข ให้ print    ยังไง print -   ยังไง print x 
        if j < 3-i:  # ลบ  i  เพื่อลดค่า -   รอบแรกก็ print -  -->> 3-0, 3-1,3-2,3-3
            print('-',end='')   
        else :
            print('x',end='')   
    print() '''
    
 #105 
'''
xxxxxxx
-xxxxx
--xxx
---x
'''
#logic  x -2 , - +1    7 -1
'''
for i in range(4):
    for j in range(8-i):
        if j>i  :
            print('x',end='')
        else:
            print('-',end='')
    print()
   '''  
   
#106  7 low 7 colume
# *** ใช้ เงื่อนไข or  เพื่อต้องการผลลัพธื ที่ แตกต่างกัน    
'''
x-----x
-x---x-
--x-x--
---x---
--x-x--
-x---x-
x-----x
'''
'''
for i in range(7):
    if i <=6:    # เงื่อนไขตรงนี้ ก็สำคัญ เพื่อจำกัด การใช้งาน Loop 
        for j in range(7):
            if i==j or i+j==6:   # สำคัญมากใน ตรงนี้   ถ้า i=3 +j =3 ==6   
                print('x',end='')
            else:
                print('-',end='')
            
    print() 

'''

#107 
'''
---x---
--x-x--
-x---x-
x-----x
-x---x-
--x-x--
---x---
'''
#การนำ function abs()  มาใช้ 
#abs ย่อมาจาก absolute โดยจะ return ผลบวกของตัวเลข แต่หากใส่ argument เป็นเลขจำนวนซ้อน จะ return ขนาดของเลขจำนวนซ้อนนั้นๆ
'''
for  i in range(7):
    if i<=6:
        for j in range(7):
            if (j==abs(3-i)) or (j==6-abs(3-i)):
                print('x',end='')
            else:
                print('-',end='')
                
        print()'''

#108  # print by while loop 
'''
---------x
--------x
-------x
------x
-----x
----x
---x
--x
-x
x

'''

# for loop
'''
for i in range(9,-1,-1):  #0-9   10 low
    for j in range(i+1):   #เริ่มที่ 0 จบรอบที่ i+1(10) -> 9+1  10  ค่า i ลดลง  8+1 ,7+1 ...   
        if j==i: #  10 == 9+1  ,   9 == 8+1 
            print('x',end='')
        else:
            print('-',end='')
    print()
'''

#109   low 10 column 10 

'''
---------x
--------xx
-------xxx
------xxxx
-----xxxxx
----xxxxxx
---xxxxxxx
--xxxxxxxx
-xxxxxxxxx
xxxxxxxxxx
'''
'''
for i in range(9,-1,-1):
    for j in range(10):
        if j ==i or j>i: 
            print('x',end='')
        else:
            print('-',end='')
    print() 
    
'''


#110 low 10 column 10+10  
# เพิ่มค่า x  จากโจทย์ 109 
'''
---------x
--------xxx
-------xxxxx
------xxxxxxx
-----xxxxxxxxx
----xxxxxxxxxxx
---xxxxxxxxxxxxx
--xxxxxxxxxxxxxxx
-xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxx
'''
'''
for i in range(10):  # low 10 เหมือนเดิม
    for j in range(10+i): # column เริ่ม 10  เพิ่มตามตามค่า i   print x  
        if i+j >=9:   # ถ้าค่า i+j >=9  -> 0+0 >=9  F print -  , 0+9 ==9 print x  ,loop j  ที่เพิ่มค่า i  ไป 1  ในรอบ 2 ก็จะเพิ่มค่า x  ไป 1 ....
            print('x',end='')
        else:
            print('-',end='')
    print() 
'''


#112 low 10 column 10    print number  *** Logic ดีๆ 
'''
--------1
-------12
------123
-----1234
----12345
---123456
--1234567
-12345678
123456789
'''
'''
for  i in range(1,10):
    number =1
    for j in range(1,10):
        if i+j >=10:  # 1+9 true  print number 
            print(number ,end='')
            number = number +1 # number += 1
        else:
            print('-',end='')
    print()
    
# loop logic  ดีๆ 
# i=1
 #  i(1) +j(2)  f  print - 
# 1+9   T  print number (1)   จบ loop  i = 1 

#  i=2
# 2+ 1..7  F print -    ,   2+8 T print  number =1 ,  2+9 >=10 T print number  = 2  
# *** แปรผัน ตาม ค่า i  และ True ,False 
'''

#113  print number  แบบ ย้อนกลับ *** good logic
#  สร้าง ตัวเลขที่มีการ เพิ่มค่า และ ลดค่า จากการกำหนด เงื่อนไข loop  และ if  elif else 
'''
- - - - - 1
------- 121
------12321
-----1234321
----123454321
---12345654321
--1234567654321
-123456787654321
12345678987654321

'''

'''
for  i in range(9):# กำหนดให้ 0-8  ก็คือ 9  low 
    number =0 # ตัวแปร ในการ print number  
    
    for j in range(9+i): # กำหนด ให้ Column  คือ 0-9  + รอบของ i 
        
        if ( i+j >=8) and ( j<=8):  #  0+7 = 8  หรือมากว่า 8 และ j <=8  T   เพิ่มค่า number  ->print number 
            number = number +1
            print(number ,end=' ')
            
        elif (i+j>=8) and (j>8):
            number = number-1
            print( number ,end=' ')
            
        else:   #เงื่อนไข ที่ ไม่ตรงกับ if  และ elif  print - 
            print('-',end=' ')
    print()

    # ***  การกำหนด เงื่อนไข เร่ิมต้น จบ Loop  เพื่อนำ ไป แปรผัน ในเงื่อนไข   loop  i  สำคัญเสมอ 
    # ***  การกำหนด เงื่อนไข เร่ิมต้น จบ Loop  เพื่อนำ ไป แปรผัน ในเงื่อนไข   loop  i  สำคัญเสมอ 
    
    #  i =0  ->   0+8  and 8<=8    print number+1 = 1   ->print 1   
    # i =1 -> 1+7 and 7<=8  print num =1 ->print 1  ,  1+8 and 8<=8  print num = 1+1 -> 2    , 1+9 and 9>8 (elif )  print num=2-1 ->  1  
'''

#114   low 5  colume 5+4    เพิ่ม column ที่ละๅ  ค่า num  เพิ่มที่ละ 2  print สลับ 
''' 
----1
---123
--54321
-1234567
987654321
'''
'''
for i in range(5): # low 5
    if i%2 ==0:  # ถ้า Low เป็นเลขคู่
        number = 2*i+1  #  num = 2*(0,2,4) +1
        for j in range(5+i):  # 0-4  + (0,2,4) 
            if i+j >=4:  #  (0,2,4) +j = 4  
                print( number, end='')   # 
                number = number -1
            else:
                print('-', end='') 
        print() 
    else:
        number =1
        for j in range(5+i):
            if  i+j >=4:
                print( number , end='')
                number = number +1
            else:
                print('-',end='') 
        print() 
'''

#115 low5  column 5
'''
----1
---12
--543
-1234
98765
'''

for i in range(5): # low 5
    if i%2 ==0:  # ถ้า Low เป็นเลขคู่
        number = 2*i+1  #  num = 2*(0,2,4) +1
        for j in range(5):  # 
            if i+j >=4:  #  (0,2,4) +j = 4  
                print( number, end='')   # 
                number = number -1
            else:
                print('-', end='') 
        print() 
    else:
        number =1
        for j in range(5):
            if  i+j >=4:
                print( number , end='')
                number = number +1
            else:
                print('-',end='') 
        print()
    #logic

    