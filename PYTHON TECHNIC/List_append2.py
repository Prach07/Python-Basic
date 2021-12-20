#ex49 (2)  list1=[1,2,3,4,5,6,7,8,9,10] input Num1 integer check Num1 in list1? Y  del  N append and print list1

list1=[1,2,3,4,5,6,7,8,9,10] 
Num1=int(input("enter integer:"))
if Num1 in list1:
    index=list1.index(Num1)  # put number to index
    del list1[index]
else:
    list1.append(Num1)
    
print(list1)