import numpy as np

class MinimosQuadrados:

    def __init__(self, x, grau):
        self.t = self.ler_dados()
        self.grau = grau
        self.y = []
        self.g = []
        self.gt_g = []
        self.gt_y = []
        
    def ler_dados(self):
        return [(-1, 1), (-0.5, 0.5), (0, 0), (0.5, 0.5), (1, 2)]

    def getLinha(self,matriz, n):
        return matriz[n]

    def getColuna(self,matriz, n):
        return [i[n] for i in matriz]   

    def cria_matriz(self):

        for valor in self.t:
            self.y.append(valor[1])

            self.g.append([valor[0]**i for i in range(self.grau+1)])
        self.gT = (np.array(self.g).T).tolist()

        for i in range(len(self.gT)):
            self.gt_g.append([])
            for j in range(len(self.g[0])):
                soma = [x*y for x,y in zip(self.getLinha(self.gT, i), self.getColuna(self.g, j))]
                self.gt_g[i].append(sum(soma))

        for i in range(len(self.gT)):
            soma = 0
            for j in range(len(self.y)):
                soma += (self.gT[i][j] * self.y[j])
            self.gt_y.append(soma)

        
    
        print(np.linalg.solve(self.gt_g,self.gt_y))

MinimosQuadrados(1,2).cria_matriz()
