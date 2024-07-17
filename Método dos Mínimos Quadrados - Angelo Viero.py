import numpy as np
import matplotlib.pyplot as plt

def gauss(A, b):
    n = len(b)
    M = A.copy()

    for k in range(n):
        for i in range(k+1, n):
            if M[i, k] == 0.0:
                continue
            fator = M[i, k] / M[k, k]
            for j in range(k, n):
                M[i, j] = M[i, j] - fator * M[k, j]
            b[i] = b[i] - fator * b[k]
    
    x = np.zeros(n)
    x[-1] = b[-1] / M[-1, -1]
    for i in range(n-2, -1, -1):
        soma_ax = 0
        for j in range(i+1, n):
            soma_ax += M[i, j] * x[j]
        x[i] = (b[i] - soma_ax) / M[i, i]
    
    return x

def soma_potencias(x, potencia):
    return sum([val ** potencia for val in x])

def soma_produtos(x, y, potencia):
    return sum([y[i] * (x[i] ** potencia) for i in range(len(x))])

def interpolacao(x, y, grau):
    n = len(x)
    
    # Construindo a matriz A
    A = np.zeros((grau + 1, grau + 1))
    B = np.zeros(grau + 1)

    for i in range(grau + 1):
        for j in range(grau + 1):
            A[i][j] = soma_potencias(x, i + j)
        B[i] = soma_produtos(x, y, i)
    
    #sistema linear Ax = B usando eliminação de Gauss
    coeficientes = gauss(A, B)
    
    #definindo o polinômio interpolador
    def p(x_valor):
        return sum(coeficientes[i] * x_valor ** i for i in range(grau + 1))
    
    return p, coeficientes

def main():
    grau = int(input("Insira o grau do polinômio (até 4): "))

    if grau < 1 or grau > 4:
        print("Este programa suporta apenas polinômios de grau entre 1 e 4.")
        return

    n = int(input("Insira o número de pontos de dados: "))

    x = []
    y = []
    print("Insira os valores de x e y:")
    for i in range(n):
        x.append(float(input(f"x[{i}]: ")))
        y.append(float(input(f"y[{i}]: ")))

    # Calculando o polinômio interpolador
    p, coeficientes = interpolacao(np.array(x), np.array(y), grau)
    
    print(f"Coeficientes do polinômio interpolador: {coeficientes}")

    # Plotando os pontos (x, y) e o polinômio interpolador
    x_plot = np.linspace(min(x), max(x), 100)
    y_plot = [p(xi) for xi in x_plot]

    plt.scatter(x, y, color='red', label='Pontos dados')
    plt.plot(x_plot, y_plot, label='Polinômio interpolador')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Interpolação Polinomial')
    plt.show()

if __name__ == "__main__":
    main()
