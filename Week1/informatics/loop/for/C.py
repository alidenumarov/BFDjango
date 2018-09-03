import math
a = int(input())
b = int(input())
for x in range (a,b+1):
   s = math.sqrt(x)
   if int(s)*int(s)==x:
      print (x,end=" ")