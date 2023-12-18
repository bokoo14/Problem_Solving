#11664 선분과 점
#2022.08.17
import sys
import math
input=sys.stdin.readline

#선분의 양 끝점 :A, B  점의 좌표: C
ax, ay, az, bx, by, bz, cx, cy, cz=map(int, input().split())

#두 점 사이의 길이 구하기
def lenC(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)


ans=1e9
while True:
     mx,my,mz = (ax+bx)/2,(ay+by)/2,(az+bz)/2
     l = lenC(ax, ay, az, cx, cy, cz)
     h = lenC(mx, my, mz, cx, cy, cz)
     r = lenC(bx, by, bz, cx, cy, cz )

     if abs(ans-h) <= 1e-6:
         print('%0.10f'%ans)
         exit()

     if h < ans:
         ans = h
     if l > r:
         ax,ay,az = mx,my,mz
     else:
         bx,by,bz = mx,my,mz

         

'''
lenmin=1e9
def binary(x1, y1, z1, x2, y2, z2):
    global lenmin
    
    AC=lenC(x1, y1, z1, cx, cy, cz)
    BC=lenC(x2, y2, z2, cx, cy, cz)
    midlen=lenc((x1+x2)/2, (y1+y2)/2, (z1+z2)/2,x1+x2)/2, (y1+y2)/2, (z1+z2)/2 )
    
    if :
        return

    if AC<BC: #AC가 더 작으면 AC쪽으로 자르기
        binary(x1, y1, z1, (x1+x2)/2, (y1+y2)/2, (z1+z2)/2)
    elif AC>BC: #BC가 더 작으면 BC쪽으로 자르기
        binary((x1+x2)/2, (y1+y2)/2, (z1+z2)/2, x2, y2, z2)
        
    
    
print(lenmin)

'''
