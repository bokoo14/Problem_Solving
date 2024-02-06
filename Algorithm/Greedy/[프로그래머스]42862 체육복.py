def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 여벌을 갖고 왔지만 도난당한 경우
    for reserveStudent in reserve[:]:  # Use a copy of the list
        if reserveStudent in lost:
            reserve.remove(reserveStudent)
            lost.remove(reserveStudent)

    for reserveStudent in reserve:
        left = reserveStudent - 1
        right = reserveStudent + 1
        if left in lost:
            lost.remove(left)
        elif right in lost:
            lost.remove(right)

    answer = n - len(lost)
    return answer
