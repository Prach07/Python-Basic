#10  เขียนฟังก์ชั่น ลบคำ จากสายอักขระ และ return ออกมา   . function input 2 parameter  -> str1 , str2  
#ตัวอย่่าง   str1 = 'onetwothree'   and str2 = 'two'   return  'onethree'    

def  Rmove_string(str1, str2):
    return str1.replace(str2, '')

Rmove_string('onetwothree', 'two')  # send parameter to function Rmove_string  # 'onethree'

