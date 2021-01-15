from collections import defaultdict

arr = [1, 3, 9, 9, 27, 81]
r = 3

def countTriplets(arr, r):
    v2 = defaultdict(int)
    print(v2)
    v3 = defaultdict(int)
    print(v3)
    count = 0
    for k in arr:
        count += v3[k]  # v3[k] é a qunatidade de triplets que k completa
        v3[k*r] += v2[k] # v2[k] é a quantidade de elemento do meio que k é, por isso v3[k*r] é a quantidade de triplets que k*r completa, uma hora k*r vai ser um k (ou nao), pode ser que k*r nunca surja no arr
        v2[k*r] += 1 # Diz que k*r vai ser o elemento do meio por k existir, ou seja, k existe logo k*r é o elemento do meio e v2[k*r] simboliza quantas vezes isso vai acontecer
        print(f'k = {k}')
        print(f'v2 = {v2}')
        print(f'v3 = {v3}')


    return count

result = countTriplets(arr, r)
print(result)