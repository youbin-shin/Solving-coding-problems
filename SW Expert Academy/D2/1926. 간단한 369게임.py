N = int(input())
N_str = ''
for n in range(1, N+1):
    N_str += str(n) + ' '

N_str = N_str.replace('3','-')
N_str = N_str.replace('6','-')
N_str = N_str.replace('9','-')
for i in range(1, 10):
    b = str(i)+'-'
    N_str = N_str.replace(b, '-')
for i in range(10):
    a = '-'+str(i)
    N_str = N_str.replace(a, '-')
print(N_str)