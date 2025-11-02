def missing_num(num):
    n = len(num) + 1   
    total = n * (n + 1) // 2
    actual = sum(num)
    return total - actual

num = [1, 3, 4]
print("The missing number is", missing_num(num))


