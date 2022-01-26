from datetime import *

today = date.today()
print(today)
eoy = date(2022, 12, 31)
diff = eoy - today
now = datetime.now()
now = now.strftime("%m/%d/%Y")
print(now)

