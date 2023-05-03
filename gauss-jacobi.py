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
    raise Exception("O método de Gauss-Jacobi não convergiu")

A = [[1, 10, 3], [7, 5, 8], [2, 3, 4]]
b = [5, 4, 10]
x0 = [0, 0, 0]
x = gauss_jacobi(A, b, x0)
print(x)
