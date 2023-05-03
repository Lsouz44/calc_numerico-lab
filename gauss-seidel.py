import numpy as np

# Define o sistema linear como uma matriz e um vetor
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
b = np.array([1, 3, -2])

# Define a tolerância e o número máximo de iterações
tol = 1e-10
max_iter = 1000

# Define os valores iniciais das variáveis
x = np.zeros_like(b)

# Implementa o método de Gauss-Seidel
for i in range(max_iter):
    x_old = np.copy(x)
    for j in range(len(b)):
        x[j] = (b[j] - np.dot(A[j,:j], x[:j]) - np.dot(A[j,j+1:], x_old[j+1:])) / A[j,j]
    if np.linalg.norm(x - x_old) < tol:
        break

# Imprime a solução
print("Solução:")
print(x)
