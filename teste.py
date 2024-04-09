import math

def f(x):
    return 3 * x - 2.71828**-x  # Função para a qual queremos encontrar a raiz

def df(x):
    return 3 + 2.71828**-x # Derivada da função f(x)



def newton_raphson(f, df, x0, tol = 0.01, max_iter = 10):
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

# Chamada da função para encontrar a raiz
x0 = 1.5  # Estimativa inicial
newton_raphson(f, df, x0)
