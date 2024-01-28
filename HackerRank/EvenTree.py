import math
import os
import random
import re
import sys

# 노드의 개수, 엣지 개수, 자식 노드, 부모 노드
def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = [[] for _ in range(t_nodes+1)] # 연결된 트리 생성
    for (index, value) in zip(t_to, t_from):
        tree[index].append(value)
    
    subTreeNodeNum = [1]*(t_nodes+1) # 하위 트리의 노드 개수 저장
    for i in reversed(range(1, t_nodes+1)):
        if tree[i]!=[]: # 연결된 노드가 있다면? (하위 노드가 있다면)
            for subTreeNode in tree[i]:
                subTreeNodeNum[i] += subTreeNodeNum[subTreeNode]
    
    answer = 0
    for check in subTreeNodeNum:
        if check%2==0:
            answer += 1
    
    # 나눠질 수 있는 서브트리의 수를 구한 것이기 때문에, 1을 뺴줘야 edge의 개수를 구할 수 있다.
    return answer-1


print(evenForest(10, 9, [10, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 3, 2, 1, 2, 6, 8, 8]))

'''
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
'''