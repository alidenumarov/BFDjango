n = int(input())
 
a = [int(x) for x in input().split()]
 
cnt = 0
 
ok = 0
for i in range(1,n):
   if a[i]<0 and a[i-1]<0:
      ok = 1
   if a[i]>=0 and a[i-1]>=0:
      ok = 1
 
if ok==1:
   print("YES")
else:
   print("NO")