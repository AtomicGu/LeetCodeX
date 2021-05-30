N, K = map(int, input().split())
HW = []
for i in range(N):
    H, W = map(int, input().split())
    HW.append((H, W))
HW.sort(reverse=True)


def check_side_length(l):
    n = 0
    for H, W in HW:
        if H < l:
            return False
        n += (H // l) * (W // l)
        if n >= K:
            return True
    return False


max_side_length = 1
l = 2
dl = 8
while True:
    if check_side_length(l):
        max_side_length = l
        l += dl
    elif dl == 1:
        break
    else:
        dl >>= 1
        l -= dl

print(max_side_length)
