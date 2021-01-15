if __name__ == '__main__':
    s = input()
    x = [False for i in range(5)]
    for c in s:
        if c.isalnum():
            x[0] = True
        if c.isalpha():
            x[1] = True
        if c.isdigit():
            x[2] = True
        if c.islower():
            x[3] = True
        if c.isupper():
            x[4] = True
    for bool in x:
        print(bool)



