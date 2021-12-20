#67 list1=['one','two',''three'',''forur''] , list2=[1,2,3,4]  สร้าง dictionary ที่มี key  เป็นสมาชิก list1 
# และมี value เป็นสมาชิก list2  and print dictionary ออกมา


list1=['one','two','three','forur'] 
list2=[1,2,3,4] 
n=len(list1)
dic1={} 

for i in range(n): # ความยาวของ list1 
    dic1[list1[i]]= list2[i]
# output 
print(dic1)
