# calc_numerico-lab
Atividades de Laboratório da disciplina de Cálculo Numérico

*** 1ª atividade ***

Desenvolver um programa que seja capaz de encontrar uma raiz aproximada de uma função real dados:
- Uma função;
- Um valor inicial;
- Uma precisão desejada.

Implementar dois métodos:
I) Bisseção ou Falsa Posição;
II) Newton ou secante.

Plotar o erro a cada iteração usando cada um dos métodos, para que seja possível uma comparação da convergência.


Utilizando qualquer linguagem de programação
Utilizando qualquer biblioteca auxiliar.
(a biblioteca pode ser usada para manipulação de estruturas de dados e funções básicas, mas o método precisa ser implementado)


*** 2ª atividade ***

Utilizando qualquer linguagem de programação, implementar um programa capaz de encontrar a solução de um sistema linear usando:
- Gauss-Jacobi
- Gauss-Seidel

Entrada:
1 10 3        x1 + 10x2 + 3x3 = 5
7 5 8   =>    7x1 + 5x2 + 8x3 = 4
2 3 4         2x1 + 3x2 + 4x3 = 10
5
4
10

Algumas coisas secundárias (que são interessantes)

1 - Calcular o erro após cada iteração
2 - Plotar as evoluções dos erros
 
     ^
     | x
     |   x
erro |     
     |       x
     |____________ x____x___>
            iteração
          

Caminho para resolver de uma forma fácil:

1 - Ler os valores de entrada e armazenar A como matriz e b como vetor.

2 - Gauss-Jacobi (slide 56)
- Calcular a matriz C;
- Calcular o vetor G;
- x^(k+1) = Cx^(k) + G;
  
Gauss-Seidel (slide 63)
- Calcular L, R e D;
- x^(k+1) = D^(-1)b - D^(-1)Lx^(k+1) - D^(-1)Rx^(k);



*** 3ª atividade ***

Método de Newton para interpolação polinomial

-> Entrada: conjunto de n+1 pontos (Xk, f(Xk))
             ponto x̅ 
             
-> Saída: Pn( x̅ ) usando polinômio de Newton

Para fazer o polinômio, vamos precisar das diferenças divididas, o que pode ser por:
• Tabela de diferenças divididas
• Função recursiva



*** 4ª atividade ***

Mínimos quadrados
Implementar um programa que:

1- Receba um conjunto de pontos unidimensionais (Xk, f(Xk)), um grau desejado n e um valor de x qualquer e calcule α(x) através de um polinômio de grau n.

2- Receba um conjunto de pontos P-dimensionais e calcule α(x) para um X P-dimensional qualquer.
_______________________________________________________________________________________________________

Durante a solução, alguns passos serão:

1- Leitura dos dados
-> Pode ser feita da forma mais conveniente

2- Cálculo do (G^t)G e do (G^t)y
-> Multiplicação de matrizes **eu quero que vocês implementem**
for   ] -> para cada posição
 for  ]       da matriz
   for ] -> produto interno

3- Resolução do sistema (G^t)G*α = (G^t)y
-> Pode usar biblioteca (numpy resolve)
