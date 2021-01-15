from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print("a = {}".format(a))
        b = Counter(a)
        print("b = {}".format(b))
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
