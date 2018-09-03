if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        op, *params = input().split()
        cur = list(map(int, params))
        if op == 'insert':
            arr.insert(cur[0], cur[1])
        elif op == 'remove':
            arr.remove(cur[0])
        elif op == 'append':
            arr.append(cur[0])
        elif op == 'sort':
            arr.sort()
        elif op == 'pop':
            arr.pop()
        elif op == 'reverse':
            arr.reverse()
        else:
            print(arr)