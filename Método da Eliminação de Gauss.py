import numpy as np

def gauss(A, b):
    n = len(b)

    #Eliminação
    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            b[i] = b[i] - m * b[k]

    #Resolução do sistema triangular superior
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]

    #Arredondamento
    x = np.round(x, decimals=5)

    return x

"""

#Validação do Código
A = np.array([[3, 2, 4],
              [1, 1, 2],
              [4, 3, -2]], dtype = float)

b = np.array([1, 2, 3], dtype = float)
"""

"""
#Exemplo 1
A = np.array([[2, 2, 1, 1],
              [1, -1, 2, -1],
              [3, 2, -3, -2],
              [4, 3, 2, 1]], dtype = float)

b = np.array([7, 1, 4, 12], dtype = float)
"""

#Exemplo 3
A = np.array([[3, -2, 5, 1],
              [-6, 4, -8, 1],
              [9, -6, 19, 1],
              [6, -4, -6, 15]], dtype = float)

b = np.array([7, -9, 23, 11], dtype = float)

x = gauss(A, b)
print("Solução: ", x)
