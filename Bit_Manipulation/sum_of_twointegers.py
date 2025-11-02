#sum of two integers

def sum_of_two_integrs(a,b):
    mask=0x7FFFFFFFF
    MAX_INT=0xFFFFFFFF
    while b!=0:
        sum_=(a^b)&mask
        carry=((a&b)<<1)&mask
        a,b=sum_,carry
    if a<=MAX_INT:
        return a
    else:
        return ~(a^mask)
a=4
b=7
print(sum_of_two_integrs(a,b))