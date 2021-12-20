#  หาค่าเฉลี่ย avg , มัธยฐาน และ ฐานนิยม โดย import statistics 
#32 เขียน Function หาค่าเฉลี่ย avg , มัธยฐาน และ ฐานนิยม  return 3 result .  input 1 parameter  -> listA ที่มีสมาชิกเป็นจำนวนใดๆ 

def Find_avg_median_Mode( listA ):
    import statistics   #   ไม่ต้องนั่ง code ตาม logic  เลย 
    meanA = statistics.mean(listA)
    medianA= statistics.median(listA)
    modeA= statistics.mode(listA)
    return meanA, medianA, modeA

#รับ return  จากการเรียกใช้ ฟังก์ชั่น  ใส่ในตัวแปร เพื่อทำการ Print โดยมี การระบุ ของตัวแปรแต่ละชนิด
mean, median, mode = Find_avg_median_Mode( [1,2,2,3,4] )

print('mean = ', mean)  #2.4
print('median= ',median) #2
print('mode = ',mode)  # 2
    