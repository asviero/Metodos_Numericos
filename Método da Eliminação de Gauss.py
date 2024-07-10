import numpy as np

def gauss(A, b):
    n = len(b)
    index = np.arange(n)  #Para rastrear as trocas de colunas

    #Eliminação
    for k in range(n - 1):
        #Pivoteamento completo
        #Encontra o índice do maior valor absoluto na submatriz A[k:n, k:n]
        max_index = np.unravel_index(np.argmax(abs(A[k:n, k:n])), A[k:n, k:n].shape)
        max_row = max_index[0] + k
        max_col = max_index[1] + k

        #Troca a linha k com a linha max_row
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        
        #Troca a coluna k com a coluna max_col
        if max_col != k:
            A[:, [k, max_col]] = A[:, [max_col, k]]
            index[[k, max_col]] = index[[max_col, k]]
        
        #Verifica se o pivô é zero após a troca
        if A[k, k] == 0:
            print("O sistema não tem solução única")
            return None

        #Eliminação
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            b[i] = b[i] - m * b[k]

    #Resolução do sistema triangular superior
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i] 

    #Reordena a solução de acordo com as trocas de colunas
    x_temp = np.zeros(n)
    for i in range(n):
        x_temp[index[i]] = x[i]
    x = x_temp

    #Arredondamento
    x = np.round(x, decimals=5)

    return x

#Exemplo 3
A = np.array([[3, -2, 5, 1],
              [-6, 4, -8, 1],
              [9, -6, 19, 1],
              [6, -4, -6, 15]], dtype = float)

b = np.array([7, -9, 23, 11], dtype = float)

x = gauss(A, b)
print("Solução: ", x)
