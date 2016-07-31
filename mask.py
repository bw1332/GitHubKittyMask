import os
from datetime import datetime

def commit(days):
    f = open("kitty",'a')
    f.write("cat")
    f.close()
    os.system("git add -A")
    os.system("git commit --date='{0} day ago' -m 'kitty'".format(str(days)))

kitty = [
         [0,9,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,9,9,0,0,9,9,0,0,0,0,0,0,0,0,0,0,0,3],
         [6,9,9,9,9,9,9,6,3,3,3,3,3,3,3,0,0,3,0],
         [0,9,0,9,9,0,9,0,0,0,0,0,0,0,0,3,3,0,0],
         [6,9,9,9,9,9,9,6,0,0,0,0,0,0,0,3,0,0,0],
         [0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,0,0,0,0],
         [0,0,0,0,0,9,0,9,0,0,0,0,0,9,0,9,0,0,0]
         ]

row = len(kitty)
col = len(kitty[0])

dayOfWeek = datetime.now().weekday()
if dayOfWeek == 5
    dayOfWeek = 0
elif dayOfWeek == 6
    dayOfWeek = 1
else
    dayOfWeek = dayOfWeek + 1
days = dayOfWeek + 7 * 6

if os.path.exists("kitty"):
#right cat
    for c in range(col):
        for r in range(row):
            times = kitty[row - r - 1][col - c - 1]
            while times > 0:
                times -= 1
                commit(days)
            days += 1

#left cat
    days += 7 * 5

    for c in range(col):
        for r in range(row):
            times = kitty[row - r - 1][c]
            while times > 0:
                times -= 1
                commit(days)
            days += 1
