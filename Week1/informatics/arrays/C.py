n = int(input())
 
a = [int(x) for x in input().split()]
 
cnt = 0
for i in range(n):
   if a[i]>0:
      cnt = cnt+1
 
print (cnt)