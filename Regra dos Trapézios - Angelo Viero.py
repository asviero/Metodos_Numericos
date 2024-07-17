import math

def regra_trapezios(f, a, b, n):
    #tamanho de cada subintervalo
    h = (b - a) / n

    print(f"Tamanho (h) de cada intervalo: {h}\n")
    
    #pontos X e Y para os trapézios
    X = [a + i * h for i in range(n + 1)]
    Y = [f(x) for x in X]
    
    print("   xi    | f(xi) = √xi")
    print("-------------------------")
    for i in range(len(X)):
        resultado = f"{Y[i]:.3f}"
        print(f"x{i} = {X[i]:.1f} | √{X[i]:.1f} = {resultado}")
    
    #soma dos trapézios
    soma_interna = sum(Y[1:n])
    integral = (h / 2) * (Y[0] + 2 * soma_interna + Y[n])
    integral = round(integral, 3)

    #imprime a fórmula da integral dos trapézios com os valores e o resultado da integral aproximada
    Y_2 = ' + '.join([f"{y:.3f}" for y in Y[1:n]])
    formula_integral = f"Integral ≈ {h/2:.3f} * [{Y[0]:.3f} + 2 * ({Y_2}) + {Y[n]:.3f}]"
    print("\nFórmula da Integral dos Trapézios:")
    print(f"\nIntegral ≈ h/2 * [f(x0) + 2 * (f(x1) + f(x2) + f(x3) + f(x4)) + f(x5)]")
    print(formula_integral)
    print(f"\nResultado da Integral ≈ {integral}")
    
    return integral

def funcao(x):
    return math.sqrt(x)

a = 1
b = 2 #a,b: intervalo
n = 5 #n: nº trapézios
integral_aproximada = regra_trapezios(funcao, a, b, n)
