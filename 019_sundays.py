from datetime import date 
from datetime import timedelta

start = date(1901, 1, 1)
end = date(2000, 12, 31)
count = 0
while start < end:
    if start.weekday() == 6 and start.day == 1:
        count += 1
    start += timedelta(days=1)

print(count)
