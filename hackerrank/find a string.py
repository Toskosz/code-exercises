def count_substring(string, sub_string):
    x = 0
    for i in range(0, (len(string) - len(sub_string) + 1)):
        if string[i:i + len(sub_string)] == sub_string:
            x = x + 1
        print(string[i:i + len(sub_string)])
    return x


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
    

# Usando list comprehension :
#
# string, substring = (input().strip(), input().strip())
# print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))