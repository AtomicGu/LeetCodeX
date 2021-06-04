from datetime import date, timedelta

td_1day = timedelta(1)

begin = date(1900, 1, 1)
end = date(9999, 12, 31)


now = begin
counter = 0
while now < end:
    if "2" in now.strftime("%Y%m%d"):
        counter += 1
    now += td_1day

counter += 1  # 9999/12/31
print(counter)

# 1994240
