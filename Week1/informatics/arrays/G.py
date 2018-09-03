n = int(input())
 
a = [int(x) for x in input().split()]
 
cnt = 0
 
ok = 0
 
 
for x in range(0,n):
   print(a[n-x-1],end=" ")
 