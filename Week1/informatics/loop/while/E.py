import math
n = int(input())
i = 1
ok = 0
cnt = 0
while i<=2000000000:
   if i>=n:
      print (cnt)
      break;
   i*=2
   cnt = cnt + 1