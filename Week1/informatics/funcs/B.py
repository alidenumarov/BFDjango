def is_function(x):
    f = x[0]
    s = x[1]
    ans = 1.0
    for x in range(s):
        ans *= float(f)
 
    return ans
 
a = [int(x) for x in input().split()]
print(is_function(a))
