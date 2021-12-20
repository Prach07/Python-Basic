# 73   example by function 

def checkkey_dict( dict1, key ):   # input parameter  
    
    if key in dict1:   # check key in dictionary 
        print(dict1.get(key))     #คำสั่ง get เรียก print key 
    else:
        dict1[key]='wait for assignment'  # รูปแบบการ เพิ่ม key  
        return dict1

dict1={'apple':'52 kcal','banana':'132 kcal','carrot':'46 kcal'} 
str1 = input("enter string:")
checkkey_dict(dict1 ,str1)

#การเช็ค value 
'''
#75 dict2={'name': 'Mario','age'': '30','job':'mushroom picker'}  
#  . input 1 string check *value in dict2 . 
#  Y  print(''yes'')   N print("no'')  

dict2={'name': 'Mario','age': '30','job':'mushroom picker'} 

str1=input("enter string:")
if str1 in dict2.values(): #การเช็ค value
        print("Yes")
else:
        print("No")
'''
# การเช็ค value เพื่อ หา key
''' 
dict2={'name': 'Mario','age': '30','job':'mushroom picker'} 

str1=input("enter string:")
if str1 in dict2.values(): #การเช็ค value
    for key in dict2:   #ตรวจสอบ key ใน dict2
        if dict2[key] == str1:    # ถ้า str1 ที่เป็น value ตรงกับใน key ใด
            print(key)
        else:
            pass

'''

'''
#90 country=['Brazil','China','Germany','Japan','Sweden']  
#เขียนโปรแกรม เก็บยอดขายสินค้่า (จำนวนจริง)  ลงใน Dictionary โดย กำหนด key เป็นสมาชิกใน Country และ Value เป็น ยอดขายสินค้าของ ประเทศนั้น ๆ
#Find ยอดขายสูงสุด -> max  and print 

country=['Brazil','China','Germany','Japan','Sweden'] 
n=len(country)
# Create Dictionary empty
Dict1={}
# insert key with  index list,  and input value  with input()  
for i in range(n):
    Dict1.update({country[i]:int(input())}) # insert data to Dictionary with .update()   { index 0 by list: input integer }
print(Dict1)      
'''