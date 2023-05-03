import numpy as np
import matplotlib.pyplot as plt

# Definindo a matriz A e o vetor b
A = np.array([[1, 10, 3], [7, 5, 8], [2, 3, 4]])
b = np.array([5, 4, 10])

# Definindo o critério de parada
tolerancia = 1e-5

# Definindo o chute inicial
x_atual = np.zeros_like(b)

# Armazenando a diagonal principal de A
diagonal_A = np.diag(A)

# Inicializando as listas para armazenar os erros e as soluções
erros = []
solutions = []

# Calculando a matriz C e o vetor g
C = np.diag(diagonal_A)
C_inv = np.linalg.inv(C)
D = C - A
g = np.linalg.solve(C, b)

# Aplicando o método de Gauss-Jacobi
while True:
    x_anterior = x_atual
    x_atual = C_inv @ (D @ x_atual + g)
    erro = np.linalg.norm(x_atual - x_anterior, np.inf)
    erros.append(erro)
    solutions.append(x_atual)
    if erro < tolerancia:
        break

# Imprimindo a solução
print('Solução:')
print(x_atual)

# Plotando a evolução dos erros
plt.plot(erros)
plt.xlabel('Número de iterações')
plt.ylabel('Erro')
plt.title('Evolução dos erros')
plt.show()
