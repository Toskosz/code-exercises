banco = {}   # banco para verificar caso a palavra ja exista
inicio = 0   # demarcar o inicio da substring
maior = 0    # maior substring ate o momento

# s = string qualquer

# enumerate para sabermos onde estamos e termos o valor

for i, v in enumerate(s):
    if v in banco:  # verifica se a letra ja está no banco
        x = banco[v] + 1       # pegamos a ultima posição para verificar se esta dentro da atual substring
        if x >= inicio: #caso esteja
            inicio = x + 1 # inicio agora é a ultima posição da letra + 1
    tamanho = i - inicio + 1 # aqui calculamos o tamanho da substring
    if tamanho > maior: #verificamos se é maior que o maior
        maior = tamanho # caso seja temos um novo maior
    banco[v] = i # atualizamos a ultima posição da letra atual

print(maior)