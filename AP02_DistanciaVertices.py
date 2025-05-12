def maior_distancia(matriz):
    # Cria dicionário de conexões
    conexoes = {i: [] for i in range(len(matriz))}
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                conexoes[i].append(j)

    # Função BFS para calcular distâncias a partir de um vértice
    def bfs(inicio):
        visitado = [False] * len(matriz)
        distancia = [0] * len(matriz)
        fila = [inicio]
        visitado[inicio] = True

        while fila:
            atual = fila.pop(0)
            for vizinho in conexoes[atual]:
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    distancia[vizinho] = distancia[atual] + 1
                    fila.append(vizinho)

        return max(distancia)

    # Calcula a maior distância a partir de cada vértice
    maior = 0
    for v in conexoes:
        dist = bfs(v)
        if dist > maior:
            maior = dist

    return maior


grafo_matriz1 = [[0, 1, 1, 0, 0, 0],#vertice0
                 [1, 0, 1, 1, 0, 1],#vertice1
                 [1, 1, 0, 1, 1, 0],#vertice2
                 [0, 1, 1, 0, 1, 1],#vertice3
                 [0, 0, 1, 1, 0, 1],#vertice4
                 [0, 1, 0, 1, 1, 0]]#vertice5
grafo_matriz2 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0]]
grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0]]

print(maior_distancia(grafo_matriz1)) 
print(maior_distancia(grafo_matriz2))
print(maior_distancia(grafo_matriz3))  
