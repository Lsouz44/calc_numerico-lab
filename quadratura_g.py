import numpy as np
import math

def funcao(x):
     # Defina a função f(x) que deseja integrar
     return math.e^x  # Exemplo: f(x) = e^x

def quadratura_gaussiana(f, a, b):
    # Coeficientes e nós da quadratura Gaussiana com 3 pontos
    coeficientes = [5/9, 8/9, 5/9]
    nos = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
    
    # Transformação de variável para integrar no intervalo [a, b]
    x_trans = lambda t: (b + a) / 2 + (b - a) / 2 * t
    
    # Cálculo da integral usando a fórmula de quadratura Gaussiana
    integral = 0
    for i in range(3):
        integral += coeficientes[i] * f(x_trans(nos[i]))
    
    integral *= (b - a) / 2
    
    return integral

# Defina os limites de integração
a = 0
b = 1

# Calcula a integral usando a quadratura Gaussiana
resultado = quadratura_gaussiana(funcao, a, b)

# Imprime o resultado
print("O valor da integral é:", resultado)
