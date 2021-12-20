#19 เขียนฟังก์ชั่น เครื่องแลกเหรียญ อัตโนมัติ    รับ parameter  1 ตัว  ->amount (int)  .ให้ return dictionary ที่มี key เป็น '10','5','2','1'และ value เป็นจำนวน
#เหรียญชนิดนั้นๆ โดยต้องแลกเหรียญที่ มีค่ามากให้เสร็จก่อน 

# example 
# amout = 40  -> return  {'10':4, '5':0, '2':0, '1':0 }
# amout = 48 -> return  {'10':4, '5':1, '2':1, '1':1 }

def coin_changer(amount):
    #create list and dictionary
    coin_list = ['10','5','2','1']
    coin_dict={ '10':0, '5':0, '2':0, '1':0}
    #Exchange
    for c in coin_list: #เช็คสมาชิกใน coin_list
        if amount ==0:
            break
        else:
            n_coin =amount // int(c)   #// เป็นการหารเช่นเดียวกัน แต่ผลลัพธ์ของการหารนั้นจะตัดส่วนที่เป็นทศนิยมทิ้งไป
            coin_dict[c] = n_coin
            amount= amount - n_coin*int(c)
    return coin_dict


coin_changer(58)