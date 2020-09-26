a, b = map(int, input().strip().split(' '))
answer = ""
for i in range(b):
    answer += "*" * a
    answer += "\n"
print(answer)