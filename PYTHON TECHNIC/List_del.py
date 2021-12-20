#ex47 list1=['a','b','c','d','e','f'] input 1 integer. check num1 < last index list1 if Y del index of num1 N do not thing


list1=['a','b','c','d','e','f']
num1=int(input("enter integer:"))
if num1 < len(list1):
    del list1[num1]
print(list1)