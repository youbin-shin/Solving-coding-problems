T = int(input())
for tc in range(T):
   L, U, X = map(int, input().split())
   result = L - X

   if L < X <= U:
       result = 0
   elif X > U:
       result = -1


   print('#{} {}'.format(tc+1, result))