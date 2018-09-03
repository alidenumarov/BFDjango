def is_function(x):  
   mn = 1e9
   for i in range(4):
      if x[i]<mn:
         mn = x[i]
 
   return mn

a = [int(x) for x in input().split()]
print (is_function(a))
 