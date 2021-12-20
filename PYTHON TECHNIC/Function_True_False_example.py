#7 เขียน Function หาผลบวกจำนวน *จริง ที่เป็นสมาชิกใน list และ return result.  กำหนดให้ฟังก์ชั่นนี้รับ parameter 1  ตัว คือ listA ทีมีสมาชิกเป็ฯข้อมูลใดๆ
def SumF(listA):
    sumF=0
    for a in listA:
        if type(a) == float:  # true false    การใช้ type มาตรวจสอบ สมาชิก ว่าเท่ากับ float ไหม 
            sumF=sumF+a    # เป็นจำนวนจริง ให้เก็บค่า 
    return sumF

SumF( [ 1, 2.2, 3, 4.4, 5, 1.1 ] )