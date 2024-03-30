import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
lst = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in lst:
    result = binary_search(arr, i, 0, N-1)
    if result == None:
        print(0)
    else:
        print(1)

# 미친 개뿌듯하다 이진탐색 내 힘으로 씀 ~~~~ 하하하하하하
