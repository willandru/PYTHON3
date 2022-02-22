import numpy as np

rg= np.random.default_rng(2)

b=rg.random((2,3))
print(b)

suma= b.sum()
print(suma)

minimo=b.min()
maximo=b.max()

print(minimo)
print(maximo)

b=b.reshape(1,6)
print(b)

cum= b.cumsum()
print(cum)
