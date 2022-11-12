#2292
#2022.07.07

import sys

N=int(sys.stdin.readline())

room=1
hive=1
while N > hive:
    hive=hive+ 6*room
    room+=1
    
print(room)
