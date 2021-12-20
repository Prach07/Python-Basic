#38 list1=[1,2,3,4,5,6,7,8,9,10] print index odd number(เลขคี่ ) 

#ex1 print by index  ::  
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[::2]) #print even index

#ex2 print by for +if
for i in range(1,len(list1)+1):
    if i %2==0:
        print(i)