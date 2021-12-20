# สร้างคำซ้ำ โดย เทคนิค การต่อ stringเข้าไป แล้ว เลือกการ print ลบตัวหลัง 

# 11 Create function  สร้างคำซ้ำ  return result . send 2 parametr to function    str1 , k   is string and int 
# example :  str1 ='0ne'  and  k =3   return  óne-one-one'

def Repeat_string( str1 , k ):
    word= (str1+'-')  # การต่อ - ใน string  
    word_k = word*k
    return word_k[:-1]    # print  one-one-one-   ที่คูณบรรทัดบน  โดย เริ่ม ที่ -1 ก็คือ ไม่มี - ใน one สุดท้าย 

Repeat_string(' one' , 3) 