"""3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""


import numpy as np

# a)
a = np.array([1, 3, 5, 7])
d = a[1] - a[0]  # razão da PA
next_a = a[-1] + d  # próximo elemento da sequência
print("Próximo elemento da questao a):", next_a)

# b)
b = np.array([2, 4, 8, 16, 32, 64])
r = b[1] / b[0]  # razão da PG
next_b = b[-1] * r  # próximo elemento da sequência
print("Próximo elemento da questao b):", next_b)

# c)
c = np.array([0, 1, 4, 9, 16, 25, 36])
d = c[1] - c[0]  # razão da PA
for i in range(2, len(c)):
    if c[i] - c[i-1] != d:  # se não for uma PA, é uma sequência de quadrados perfeitos
        next_c = (int(np.sqrt(c[-1])) + 1) ** 2  # próximo quadrado perfeito
        break
else:
    next_c = c[-1] + d  # próximo elemento da PA
print("Próximo elemento da questao c):", next_c)

# d)
array = [4, 16, 36, 64]

prox_par = (2 * len(array) + 2)  # Encontre o próximo número par na sequência

prox_num = prox_par ** 2  # Calcule o quadrado do próximo número par

print("Próximo elemento da questao d):", prox_num)

# e)


def proximo_fibonacci(array):
    n = len(array)
    if n < 2:
        return 1
    else:
        return array[n-1] + array[n-2]


fibonacci_array = [1, 1, 2, 3, 5, 8]  # Exemplo de uso:
proximo_numero = proximo_fibonacci(fibonacci_array)

print("Próximo elemento da questao e):", proximo_numero)

# f)
print("Próximo elemento da questao f): 200, esse seria o proximo numero com a inicial D.")
