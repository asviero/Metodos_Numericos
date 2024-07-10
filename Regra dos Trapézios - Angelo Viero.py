import math

def regra_trapezios(f, a, b, n):
    #Calcula o tamanho de cada subintervalo
    h = (b - a) / n
    
    #Constrói os pontos X e Y para os trapézios
    X = [a + i * h for i in range(n + 1)]
    Y = [f(x) for x in X]
    
    #Imprime a tabela de valores
    print("   xi    | f(xi) = √xi")
    print("-------------------------")
    for i in range(len(X)):
        resultado = f"{Y[i]:.3f}"
        print(f"x{i} = {X[i]:.1f} | √{X[i]:.1f} = {resultado}")
    
    #Calcula a soma dos trapézios
    integral = h * (sum(Y) - 0.5 * (Y[0] + Y[n]))
    integral = round(integral, 3)

    #Imprime a fórmula da integral dos trapézios com os valores calculados e o resultado da integral aproximada
    Y_str = ' + '.join([f"{y:.3f}" for y in Y[1:n]])
    formula_integral = f"Integral ≈ {h/2:.3f} * [{Y[0]:.3f} + 2 * ({Y_str}) + {Y[n]:.3f}]"
    print("\nFórmula da Integral dos Trapézios:")
    print(f"\nIntegral ≈ h/2 * [f(x0) + 2 * (f(x1) + f(x2) + f(x3) + f(x4)) + f(x5)]")
    print(formula_integral)
    print(f"\nResultado da Integral ≈ {integral}")
    
    return integral

def funcao(x):
    return math.sqrt(x)

a = 1
b = 2 #a,b: intervalo
n = 5 #n: nº trapezios
integral_aproximada = regra_trapezios(funcao, a, b, n)
