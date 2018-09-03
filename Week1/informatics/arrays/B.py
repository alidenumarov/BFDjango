n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
   if a[i]%2==0:
      print (a[i],end = " ")