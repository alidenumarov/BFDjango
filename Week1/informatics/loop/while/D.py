import math
n = int(input())
i = 1
ok = 0
while i<=2000000000:
   if i==n:
      print ("YES")
      ok = 1
      break;
   i*=2
 
if ok==0:
   print ("NO")