def num_of_bits(n):
    c = 0
    while n:
        n &= n - 1   
        c += 1
    return c

n = 0b00000000000000000000000000010111
print(num_of_bits(n))
