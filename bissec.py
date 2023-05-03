import math

# Definir uma função
def f(x):
    return(8.0 - 4.5*(x-math.sin(x)))

# Definir um intervalo [a,b]
a = float(input("Entre com o valor 'a' do intervalo [a,b]: "))
b = float(input("Entre com o valor 'b' do intervalo [a,b]: "))

l = 0.001 # Amplitude final de [a,b]
tol = 0.0001 # Tolerancia para verificar valor próximo de 0
cont = 0 # Contador para parada de emergência do looping
Ni = 100 # Nº de iterações para parada
c = b - a # Amplitude de [a,b]

x0 = (a + b)/2.0 # Ponto médio de [a,b]

# Looping enquanto a amplitude final de [a,b] não fou atingida ou |f(x0| for maior que a tolerencia)
while(c > l or math.fabs(f(x0)) > tol):

    if(f(a)*f(x0) < 0.0):
        b = x0 # C está entre [a,x0], considere o novo [a,b]
    if(f(a)*f(x0) > 0.0):
        a = x0 # C está entre [x0, b], considere o novo [a,b]

    c = b - a
    x0 = (a + b)/2.0
    cont = cont + 1
    print("\nInteracao %i\nErro =  %f" %(cont,f(x0)))

# Parada de emergência do looping
    if(cont >= Ni):
        print("ATENCAO: RAIZ NAO ENCONTRADA")
        break

print("\n")
print("="*20)
print("\nRaiz: %f\nInteracoes: %i\nf(%f) = %f" %(x0,cont,x0,f(x0)))
