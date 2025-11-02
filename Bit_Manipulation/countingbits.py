#couting no of bits

def count_bits(n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        dp[i]=dp[i>>1]+(i&1)
    return dp
n = 4
print(count_bits(n))


