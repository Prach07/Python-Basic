#29  Function แปลงเลขฐานสิบ เป็น เลขฐาน สอง  รับ parameter 1   x (int)  return  เลขฐาน 2  ของ x   ในรูปแบบ สายอักขระ 

def to_binary(x):
    import math 
    n_bit =math.floor(math.log(x, 2))
    binary = ''
    for bit in range(n_bit, -1 ,-1):
        s = x//int( 2** bit )
        binary= binary +str(s)
        x=x -s*2**bit 
    return binary 

to_binary(7) 
#'111'