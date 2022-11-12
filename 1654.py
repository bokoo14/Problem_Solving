#1654
#2022.06.27

n = list(map(int, input().split()))
wire = []
for i in range(0, n[0]):
    wire.append(int(input()))


#이진탐색 알고리즘 <cut할 랜선의 최대 길이 선택>
#랜선을 max(wire)로 설정하고 1씩 줄이면 시간초과
def wire_cut(start, end):
    if start>end:
        return end
    
    cut=(start+end)//2
    cnt=0

    for i in range(0, n[0]):
        cnt+=wire[i]//cut

    if cnt>=n[1]:
        return wire_cut(cut+1, end)
    else:
        return wire_cut(start, cut-1)


print(wire_cut(1, max(wire)))
