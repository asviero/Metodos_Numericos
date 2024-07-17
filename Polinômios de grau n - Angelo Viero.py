import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y, xi):
    n = len(x)
    resultado = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        resultado += term
    return resultado

#pontos conhecidos (x, y)
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 0, 4])

#pontos para avaliar o polinômio interpolador
x_interp = np.linspace(min(x), max(x), 100)
y_interp = [lagrange(x, y, xi) for xi in x_interp]

#imprime a interpolação em pontos específicos
avaliar_pontos = [0.5, 1.5, 2.5, 3.0]
resultados = [lagrange(x, y, xi) for xi in avaliar_pontos]

print("Resultados da interpolação:")
for xi, yi in zip(avaliar_pontos, resultados):
    print(f"f({xi}) = {round(yi, 3)}")

#plota os pontos conhecidos e o polinômio interpolador
plt.scatter(x, y, color='red', label='Pontos conhecidos')
plt.plot(x_interp, y_interp, label='Polinômio interpolador')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Lagrange')
plt.grid(True)
plt.show()
