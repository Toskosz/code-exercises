# def count_substring(string, sub_string):
#     c=0
#     for i in range(len(string)):
#         if(string[i:i+len(sub_string)]==sub_string):
#             c = c+1
#     return c
#
# def minion_game(string):
#     banco_de_palavras = []
#     vogais = ['A', 'E', 'I', 'O', 'U']
#     pontos_stuart = 0
#     pontos_kevin = 0
#     for j in range(0, len(string)):
#         for i in range(0, (len(string)-j)):
#             substring = string[j:j+i+1]
#             if substring in banco_de_palavras:
#                 continue
#             else:
#                 banco_de_palavras.append(substring)
#             print(j, i)
#             print(substring)
#             if string[j] in vogais:
#                 # pontos_kevin += string.count(substring)
#                 pontos_kevin += count_substring(string, substring)
#                 print("pontos do kevin = {}".format(pontos_kevin))
#             else:
#                 # pontos_stuart += string.count(substring)
#                 pontos_stuart += count_substring(string, substring)
#                 print("pontos do stuart = {}".format(pontos_stuart))
#
#     if pontos_kevin > pontos_stuart:
#         print("Kevin {}".format(pontos_kevin))
#     elif pontos_kevin < pontos_stuart:
#         print("Stuart {}".format(pontos_stuart))
#     else:
#         print("Draw")
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

s = raw_input()

# vowels = 'AEIOU'
#
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
#
# if kevsc > stusc:
#     print "Kevin", kevsc
# elif kevsc < stusc:
#     print "Stuart", stusc
# else:
#     print "Draw"