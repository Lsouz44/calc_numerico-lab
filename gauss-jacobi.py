import numpy as np

# Função para resolver o sistema linear usando Gauss-Jacobi
def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
            x_old = x.copy()
            for i in range(n):
                s = 0
                for j in range(n):
                    if i != j:
                        s+= A[i][j] * x_old[j]
                x[i] = (b[i] - s) / A[i][i]
                if np.linalg.norm(x - x_old) < tol:
                    return x0
    raise Exception("O método de Gauss-Jacobi não converge após {} iterações".format(max_iter))

# Obter a entrada do usuário para a matriz
n = int(input("Digite número de equações: "))
print("Digite a matriz de coeficientes (uma linha por vez): ")
A = []
for  i in range(n):
    row = [float(x) for x in input().split()]
    A.append(row)

print("Digite o vetor b: ")
b = [float(x) for x in input().split()]

print("Digite o vetor x0: ")
x0 = [float(x) for x in input().split()]

# Resolver o sistema linear usando o método de Gauss-Jacobi
x = gauss_jacobi(A, b, x0)

# Imprimira solução
print("A solução do sistema é: ")
for i in range(n):
    print("x[{}] = {:.6f}".format(i, x[i]))
