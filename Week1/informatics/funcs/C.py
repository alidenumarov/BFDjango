def is_function(x):
    f = x[0]
    s = x[1]
 
    if f==0 and s==0:
       return 0
    if f==1 and s==1:
       return 0
    if f==1:
       return 1
    if s==1:
       return 1
       
a = [int(x) for x in input().split()]
print(is_function(a))
