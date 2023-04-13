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
     |x
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
