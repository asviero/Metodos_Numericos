import math

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            print(f"Raiz encontrada: {x} (em {i} iterações)")
            return x
        if df(x) == 0:
            print("Derivada zero encontrada. O método de Newton-Raphson falhou.")
            return None
        x = x - fx / df(x)
    print("O método de Newton-Raphson atingiu o número máximo de iterações.")
    return None

def funcao(x):
    return x**2 - 2  # Função para a qual queremos encontrar a raiz

def df(x):
    return 2*x  # Derivada da função f(x)

# Chamada da função para encontrar a raiz
x0 = 3  # Estimativa inicial
newton_raphson(f, df, x0)
