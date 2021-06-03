import datetime

counter = 0

begin = datetime.date(2000, 1, 1)
end = datetime.date(2020, 10, 1)
a_day = datetime.timedelta(days=1)

date = begin
while date <= end:
    if date.day == 1 or date.weekday == 1:
        counter += 2
    else:
        counter += 1
    date += a_day

print(counter)
