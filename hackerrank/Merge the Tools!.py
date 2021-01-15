# prestar atenção ao iter
# oque o iter significa é que se fosse por exemplo uma strin 1234 e n = 4 seria uma zip de (1, 2, 3, 4)
S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))