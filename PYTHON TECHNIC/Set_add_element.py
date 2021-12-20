#84 list1=['t','u','r','i','n','g'] and tuple1=('n','e','w','t','o','n')   . Create set1 and set2  .set1->index odd number with list1 ,set2-> index even number with tuple1
#print set1 and set2 
list1=['t','u','r','i','n','g']
tuple1=('n','e','w','t','o','n')  
#Create set empty
set1=set()  # ความหมาย ของการสร้าง set ว่าง 
set2=set()
# input index ood number with list1 to set1   by add()
for i in range(len(list1)):
    if i %2==0:
        set1.add (list1[i])  # use function add()
for i in range(len(tuple1)):
    if i %2 !=0:
        set2.add( tuple1[i])
# out put 
print("set1=",set1)
print("set2=",set2)