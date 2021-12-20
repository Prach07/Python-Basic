'''

#14   เขียนฟังก์ชั่นเพื่อหา ระยะห่าง ระหว่าง 2 จุดบนเส้นจำนวนจริง and return result  .  sent 2 parameter  to function  x1 , x2 
#(hint: ระยะห่างระหว่าง 2 จุด = |x1-x2|)

def FindResult_Hint( x1 , x2) :
    return abs(x1-x2)

FindResult_Hint(32,-18)

#15 เขียนฟังก์ชั่น หากำไรขั้นต้น และ return ผลลัพธ์ ออกมา  ฟังก์ชั่นนี้รับ parameter 2 ตัว sales , cogs(ต้นทุน)   ที่เป็น int 

def FindPofit(sales , cogs):
    return sales-cogs

FindPofit(1000, 400) 

#16 ฟังก์ชั่น ลดราาคาสินค้า return ราคาหลังได้รับสส่วนลด รับ parameter pirce, discount(%)  0-100 

def PriceDiscount( price, disC):
    result = price * disC /100  # หาส่วนลดที่ได้ จาก % discount 
    return price - result # จ่ายจริง 
 
PriceDiscount(1000,50)


#17 เขียนฟังก์ชั่น กบกระโดด  โดยรับ parameter 2   d ซึ่งเป็นระยะทางที่กบต้องการกระโดด   s  เป็นระยะกระโดดได้ 1 ครั้งของกบ  
# ให้ return จำนวนครั้งที่น้อยที่สุด ที่กบต้องกระโดด เพื่อเดินทางไปให้ได้มากกว่าหรือเท่ากับ d 

def JumbJumb( d , s):
    return d/s
    
JumbJumb( 100, 20) 

#17 

def JumbJumb(d, s):
    import math
    return math.ceil(d / s)

JumbJumb(10 ,2)

#20 Function คำนวนเงินทุน สะสม รับ parameter 3 ตัวได้แก่  เงินลงทุนเริ่มต้น(pv) , อัตราผลตอบแทนในรูป% ต่อปี (r) , จำนวนปีที่ลงทุน (n) 
# return เงินลงทุนเมื่อผ่านไปแล้ว n ปี  (คิดผลตอบแทนแบบทบต้น) 

#example 
# PV= 10000  ,r=20, n=1 -> return 12000
# PV=5000, r=15, n=3 -> return 7604.375 

def Sum_investment( PV, R, N):
    Profit_y = PV * R /100 
    result= PV+Profit_y * N
    return result

Sum_investment(5000,15,3)

#20
def calculate_FV(PV, r, n):
    FV=PV*(1+r/100)**n
    return FV

calculate_FV(1000,20,2)

#21 Function หาอัตรา ผลตอบแทนในรูป % ต่อปี โดยรับ parameter 3 ตัว  เงินลงทุนเริ่มต้น(pv) , เงินลงทุนเมื่อผ่านไป n ปี (fv) , จำนวนปีที่ลงทุน (n) 
#ให้ return ผลตอบแทนในรูป %  ต่อปี
# example   PV=10000, FV=12000, n=1 -> return 20 

def Calculate_FV(PV, FV, n ):
    Percent=(( FV/PV )**(1/n)-1)*100  # สูตรคณิตศาสตร์  
    return Percent

Calculate_FV(1000,1440,2)
    
    
# 23 Funciton  หาความยาวด้านตรงข้ามมุมฉาก และ return ผลลัพธ์ออมมา   รับ parameter 2 ตัว  a , b  ที่เป็นด้านประกอบมุมฉาก
#สูตร หาความยาวด้านตรงข้ามมุมฉาก   a**2 +b**2 ==C**2   

def Find_lenRightTriangle(a, b):
    result =( a**2 +b**2 ) **(1/2) 
    return result

Find_lenRightTriangle(3,4)

#24 Function หาระยะห่างระหว่าง จุด 2 จุด  ในระนาบ 2 มิติ และ return ออกมา ( hint: ระยะห่างระหว่าง 2 จุด = sqrt((x1-x2)**2+(y1-y2)**2) )
#กำหนดให้ Function นี้รับ parameter  4   -> x1, y1 ,x2, y2 

def Find_Hint(x1, y1, x2, y2):
    import math
    Result_hint= ((x1-x2)**2+(y1-y2)**2) **(1/2)
    return Result_hint

Find_Hint(3,4,6,8)

#25 Function หาระยะห่างระหว่าง จุด 2 จุด ใน ระนาบ n มิติ  return result (hint: euclidean distance)  .parameter-> P1, P2  is tuple  ความยาว n 

def distance_Rn(P1, P2):
    sum_square=0
    n= len(P1)
    for i in range(n):
        sum_square=sum_square + (P1[i] - P2[i]) **2
        distance = sum_square**(1/2)
        return distance
distance_Rn( (1,2,2,1), (3,4,0,-1) )  
#2.0


'''