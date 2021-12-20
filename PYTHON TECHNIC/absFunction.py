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

for  i in range(7):
    if i<=6:
        for j in range(7):
            if (j==abs(3-i)) or (j==6-abs(3-i)):
                print('x',end='')
            else:
                print('-',end='')
                
        print()