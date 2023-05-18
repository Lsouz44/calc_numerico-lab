def calcular_diferencas_divididas (x, y) :
    n = len(x)
    tabela = [[0] * n for _ in range(n)]
    for i in range(n):
        tabela[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela [i][j-1]) / (x[i+j] - x[i])
    return tabela

def interpolar_newton(x, y, ponto):
    n = len(x)
    dif_div = calcular_diferencas_divididas(x, y)
    resultado = dif_div[0][0]
    produto = 1
    for i in range(1, n):
        produto *= (ponto - x[i-1])
        resultado += dif_div[0][i] * produto
    return resultado

# Exemplo de uso
x = [1, 2, 4, 7]
y = [2, -1, 3, 0]

ponto_interpolado = 3.5
valor_interpolado = interpolar_newton(x, y, ponto_interpolado)
print(f"O valor interpolado em x = {ponto_interpolado} é y = {valor_interpolado}")
