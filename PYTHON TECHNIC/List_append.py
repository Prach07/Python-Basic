#ex35 empty list  input string to list. stop when member list = 5 .but when string have list not append 
list1=[] #empty list
count=0
#input string
for i in range(10):
    if count==5:
            break
    else:
        str=input("Enter string :")
        if str in list1:
            pass
        else:
            list1.append(str)
            count=count+1
print(list1)
    
        