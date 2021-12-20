#35  เขียน Function สำหรับ วาดรูปต่อไปนี้    รับ parameter 1 ตัว -> n  (low)

# สูตร 
#   x ภาพ x ใหญ่  if j==i or (i+j == n-1)
#  x  ข้าวหลามตัด j==abs(int ( (n-1)/2) -i) ) or (j==n-1-abs( int( (n-1)/2) -i)

''' 
n=5  
logic 
#   if j==i or (i+j == n-1)

x - - - x    # 0==0 ->  0+4 == 5-1        
- x - x -    # 1(j) ==1(i) -> 1+3(j) ==5-1 
- - x - -     # 2(j) ==2(i) 
- x - x -     # 3(i) + 1(j) == 4 -> 3(i) ==3(j) 
x - - - x     #4(i)+0 == 4,   4(j)==4(i)  

'''

def Print_x( n):
    for i in range(n):
        for j in range(n):
            if j==i or (i+j == n-1): #
                print('x',end=' ') 
            else:
                print('-',end=' ')
        print()
                
Print_x(5)


'''


# #36 เขียน ฟังก์ชั่น วาดรูปต่อไปนี้  รับ parameter 1 ตัว  n 

# '''
# example n =5 
# - - x - - 
# - x - x -
# x - - - x
# - x - x -
# - - x - -

# example n =6
# - - x x - -
# - x - - x -
# x - - - - x
# - x - - x -
# - - x x - -

# '''
# '''
# # print x  ข้าวหลามตัด j==abs(int ( (n-1)/2) -i) ) or (j==n-1-abs( int( (n-1)/2) -i)
# def draw_tree2(n):
#     if n%2 ==0:
#         for i in range(n-1):
#             for j in range(n):
#                 if ( j==abs(int ( (n-1)/2) -i) ) or (j==n-1-abs( int( (n-1)/2) -i) ) :
#                     print( 'x', end=' ')
#                 else:
#                     print( '-',end=' ') 
#             print()
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if ( j==abs(int ( (n-1)/2) -i) ) or (j==n-1-abs( int( (n-1)/2) -i) ):
#                     print('x', end=' ')
#                 else:
#                     print('-', end=' ')
#             print()
            
# draw_tree2(5)



# ''''