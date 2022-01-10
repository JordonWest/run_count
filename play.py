from datetime import *

today = date.today()
eoy = date(2022, 12, 31)
diff = eoy - today
print(diff.days)
