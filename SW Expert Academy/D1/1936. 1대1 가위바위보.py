A, B = input().split()
result = 'B'
if A == '1':
    if B == '3':
        result = 'A'
elif A == '2':
    if B == '1':
        result = 'A'
else:
    if B == '2':
        result = 'A'
print(result)