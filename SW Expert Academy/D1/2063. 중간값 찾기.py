num = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[int(num//2)])