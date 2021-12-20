#26  Function  shift->    member in list  ไปทางขวา  k step  . send parameter 2 ตัว   listA ที่เก็บข้อมูลใดๆ  k เป็นจำนวนที่ต้องการให้ shift .return listA pass shift
#example  listA=[1,2,3,4,5]  k =1 return -> [5,1,2,3,4] 

def Shift_Right( listA, k):
    k = k%len(listA)
    return listA[-k:] +listA[:-k]

Shift_Right( [1,2,3,4,5], 1)
    
    
    
Shift_Right( [1,2,3,4,5]  , 1 )  

'''
#27  Function  shift<-    member in list  ไปทางซ้าย k step  . send parameter 2 ตัว   listA ที่เก็บข้อมูลใดๆ  k เป็นจำนวนที่ต้องการให้ shift .return listA pass shift
#example  listA=[1,2,3,4,5]  k =1 return -> [5,1,2,3,4] 

def Shift_Right( listA, k):
    k = k%len(listA)  #ทำการ mod k ด้วยความยาวของ ListA เนื่องจากถ้าจำนวนครั้งที่ทำการ rotate ไป เท่ากั้บจำนวนสมาชิกใน ListA จะทำให้สมาชิกกลับมาที่เดิม
    return listA[k:] +listA[:k]

Shift_Right( [1,2,3,4,5], 1)
 



'''