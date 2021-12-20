# 10 low 10 colume print x 
'''
for i in range(10):
    for j in range(10):  #Coulume 
        print('x',end="") 
    print() # ขึ้นบรรทัดใหม่ 

'''

# Col 1 ....10 Low 10

'''for i in range(10):
    for j in range(1,1+i,+1):
        print('x',end='')
    print() 
'''

# Col 10...1   Low 10 

'''for i in range(9,-1,-1):
    for j in range(i+1):  #ค่า i ลดลงเรื่อยๆ 
        print('x',end='')
    print()'''

# 
#---x
#--xxx
#-xxxxx
#xxxxxxx

'''for i in range(4):
    for j in range(4+i):
        if j < 3-i:
            print('-',end='')
        else:
            print('x',end='')
    print()'''

# xxxxxxx
#-xxxxx
#--xxx
#---x

for i in range(4):
    for j in range(4-i):
        if j >3+i:
            print('x',end='')
        else:
            print('-',end='') 
    print()