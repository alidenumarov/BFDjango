if __name__ == '__main__':
    ans = {}
    for _ in range(int(input())):
        name, *arr = input().split()
        avg = sum(list(map(float, arr))) / 3
        ans[name] = avg
    print("{0:.2f}".format(ans[input()]))


