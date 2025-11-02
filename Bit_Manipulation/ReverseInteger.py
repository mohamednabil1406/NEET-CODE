def reverse_int(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0

    while n != 0:
        digit = n % 10
        n //= 10
        rev = rev * 10 + digit

    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0

    return rev


n = 1234
print(reverse_int(n))  
