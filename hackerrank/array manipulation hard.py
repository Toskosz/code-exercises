# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# # Complete the arrayManipulation function below.
# def arrayManipulation(n, queries):
#     lista_final = [0 for _ in range(n)]
#     for i in range(len(queries)):
#         for j in range(queries[i][0], queries[i][1]+1):
#             lista_final[j-1] += queries[i][2]
#     return max(lista_final)
#
# if __name__ == '__main__':
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     queries = []
#
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = arrayManipulation(n, queries)
#     print(result)


n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
    print(list)
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)