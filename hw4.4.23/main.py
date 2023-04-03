import numpy as np

per = np.linspace(0, 8, 9)
A = 0.228
expon1 = lambda x, a: a ** x
tmp = np.zeros((len(per), 2))
tmp1 = np.zeros((len(per), 2))
sum1 = np.zeros((1, 2))
for n, t in enumerate(per):
    tmp[n][0] = -expon1(t, A)
    tmp[n][1] = expon1(t, A)

    s = 0
    while s <= t - 1:
        tmp1[n][0] += -expon1(t - s, A)
        tmp1[n][1] += expon1(t - s, A)
        s += 1
for x in range(tmp.shape[0]):
    print(f"{tmp[x]}\t{tmp1[x]}\t{tmp[x]+tmp1[x]}")
