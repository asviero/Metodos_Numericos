import numpy as np

def fatoracao_LU(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A)

    for k in range(n):
        #Gauss para calcular U e depois o L
        for j in range(k, n):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])
        for i in range(k+1, n):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U

#Exemplo dado em aula
A = np.array([
    [3, 2, 4],
    [1, 1, 2],
    [4, 3, 2]], dtype=float)

L, U = fatoracao_LU(A)

LU = np.dot(L, U)

print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)
print("\n L x U:")
print(LU)
