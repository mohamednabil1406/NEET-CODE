#calculate the single number
def single_num(n):
    res=0
    for num in n:
        res^=num
    return res
n=[3,2,3]
print("The number of No 0f 1s bits",single_num(n))