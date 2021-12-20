# เทคนิค การค้นหา ว่า string นั้น มี อักขระพิเศษไหม  เจอ ให้ลบ  ฃ
# str1 = str1.replace(c ,'') #แทนที่อักขระพิเศษที่ปรากฏใน str1ด้วย emtpy string ''   ***** การตีความที่สำคัญ


#13  เขียนฟังก์ชั่น เพื่อตัดอักขระพิเศษ(!@#$%) ออกจากสาย อักขระ และ return result .   sent 1 parameter  -> str1   is string 
# example      str1 = '@chicken'   return 'chicken'

def findSpecial_string( str1 ):
    Special_String= '!@#$%,'
    for c in Special_String:
        str1 = str1.replace(c ,'') #แทนที่อักขระพิเศษที่ปรากฏใน str1ด้วย emtpy string ''
    return str1

findSpecial_string('chicken%')  
