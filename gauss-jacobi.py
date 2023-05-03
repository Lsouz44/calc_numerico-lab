def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x
    raise Exception(f"O método de Gauss-Jacobi não convergiu após {max_iter} iterações. Última solução encontrada: {x}")

A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
b = [1, 3, -2]
x0 = [0, 0, 0]
x = gauss_jacobi(A, b, x0)
print(x)
