n, k, T = map(int, input().split())

ans = 0

a = 1
da = (1 + n) * n // 2  # 每圈数字涨多少
dda = n * n
for i in range(T):
    ans += a
    a += da
    a %= k
    da += dda

print(ans)
