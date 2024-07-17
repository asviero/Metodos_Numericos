import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    
    for iteration in range(max_iterations):
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s1) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration
        
        x = x_new.copy()
    
    raise Exception("Convergência não alcançada dentro do número máximo de iterações")

A = np.array([[5, 2, 1], 
              [1, 4, 2], 
              [2, 1, 3]], dtype=float)

b = np.array([12, 10, 11], dtype=float)
x0 = np.zeros_like(b)

sol, iterations = jacobi(A, b, x0)

print("Solução: ", sol)
print("Iterações: ", iterations)
