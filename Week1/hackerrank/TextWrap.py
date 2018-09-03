import textwrap
def wrap(s, n):
    return textwrap.fill(s, n)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
    