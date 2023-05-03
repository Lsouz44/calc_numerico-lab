import math
 
 # Definir uma função
def f(x):
    return(x*math.exp(0.5*x) + 1.2*x - 5.0)

# Função para obter a derivada
def df(x):
    h = 0.000001
    return((f(x + h) - f(x))/h)

tol = 0.000001 # Tolerancia para verificar valor próximo de 0
Ni = 100 # Nº de iterações para parada
x0 = float(input("Entre com a aproximação inicial: ")) # Aproximação inicial
x = 0.0

i = 0 # Contador para parada de emergência do looping

# Looping enquanto a função for maior que a tolerância
while(math.fabs(f(x)) > tol):

    x = x0 - f(x0)/df(x0) # Calcula a derivada da função
    x0 = x # Atualiza o valor da aproximação para x0
    i = i + 1 # Incrementa a iteração
    print("\nInteracao %i\nErro =  %f" %(i,f(x0)))

    # Parada de emergência
    if(i >= Ni):
        print("ATENCAO: RAIZ NAO ENCONTRADA")
        break

if(i < Ni):
    print("\n")
    print("="*20)
    print("\nRaiz %f\nIteracoes: %i\nf(%f) = %f\n\n" %(x0,i,x0,f(x0)))
