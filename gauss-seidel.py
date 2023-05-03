import numpy as np

# solicitar entrada da matriz
n = int(input("Digite o tamanho da matriz: "))
print("Digite a matriz linha por linha:")
a = np.zeros((n,n))
for i in range(n):
    a[i] = [float(x) for x in input().split()]
b = np.array([float(x) for x in input("Digite os termos independentes separados por espaço: ").split()])

# definir a tolerância e as condições iniciais
tol = 1e-10
x0 = np.zeros(n)

# implementar o método Gauss-Seidel
x = x0.copy()
err = 1
while err > tol:
    for i in range(n):
        s = sum(-a[i][j] * x[j] for j in range(n) if i != j)
        x[i] = (b[i] + s) / a[i][i]
    err = np.linalg.norm(x - x0)
    x0 = x.copy()

# exibir a solução
print("A solução do sistema é:")
print(x)
