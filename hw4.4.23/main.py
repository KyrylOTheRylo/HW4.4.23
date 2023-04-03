import numpy as np

per = np.linspace(0, 5, 6)
A = 0.5
expon1 = lambda x, a: a ** x
tmp = np.zeros((len(per), 2))
for n, x in enumerate(per):
    tmp[n][0] = -expon1(x, A)
    tmp[n][1] = expon1(x, A)
print(tmp)
