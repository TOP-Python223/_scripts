from datetime import datetime, date, time, timedelta
from time import sleep

print(f"{datetime(year=2022, month=1, day=1) = }")
print(f"{datetime.now() = }")

dt1 = datetime(year=2022, month=1, day=1)
dt2 = datetime.now()

print(f"\n{dt2 - dt1 = }")
sleep(1.5)

dt3 = datetime.now()
print(f"\n{dt3 - dt2 = }")

posix_time = datetime.now().timestamp()
print(f"\n{posix_time = }\t{type(posix_time) = }")

dt4 = datetime.fromtimestamp(posix_time)
print(f"\n{dt4 = }")
print(f"{dt4.date() = }")
print(f"{dt4.time() = }")
