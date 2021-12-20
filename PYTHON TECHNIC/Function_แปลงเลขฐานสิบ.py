#28  Function แปลงเลขฐานใดๆ เป็นเลขฐาน 10  รับ parameter  2  ตัว  s -> string ให้  return จำนวนเลขฐาน 10 ของ s 
#example  s='10110'  b=2  return  22 

def to_decimal(s, b):
    converter = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }
    s = s[ ::-1].upper() 
    decimal=0
    n=len(s)
    for i in range(n):
        decimal= decimal+converter[s[i]] *b**(i)
    return decimal

to_decimal('71a', 16 )

##1818