if __name__ == '__main__':
    arr = []
    mn = 100.0
    for _ in range(input()):
        name = input()
        score = float(input())
        mn = min(mn, score)
        arr.append([score, name])

    smn = 100.0
    for i in range(n):
        if smn > arr[i][0] and arr[i][0] != mn:
            smn = arr[i][0]

    ans = [name for score, name in arr if  score == smn]
    ans.sort()
    print(*ans, sep='\n')


