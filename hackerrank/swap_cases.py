def swap_case(s):
    for c in s:
        if c.isupper():
            c.lower()
        elif c.islower():
            c.upper()
    return s

if __name__ == '__main__':
    print(input().swapcase())