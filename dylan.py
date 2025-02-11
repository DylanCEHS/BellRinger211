import time
current_time = time.localtime()

class_hr= 14
class_min = 19

current_minute = current_time. tm_min
min_left = class_min - current_minute
print("Class ends in", min_left, " minutes.")
