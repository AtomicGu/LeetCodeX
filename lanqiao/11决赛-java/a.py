def is_not_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return True
    return False


counter = 0  # ! 1 不是合数也不是素数
for i in range(2, 2021):
    if is_not_prime(i):
        counter += 1

print(counter)

# 1713
