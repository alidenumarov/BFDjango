# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
ans = arr + ['WELCOME'.center(m, '-')] + arr[::-1]
print(*ans, sep='\n')