if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))
    t = hash(tuple(arr))
    print(t)