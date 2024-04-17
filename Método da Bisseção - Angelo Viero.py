import math
import matplotlib.pyplot as plt
import numpy as np

a = float(input("Selecione o ponto a: "))
b = float(input("Selecione o ponto b: "))
tol = float(input("Selecione a tolerância: "))

def bissecao(f, a, b, tol):

    #Calcula o nº de iterações
    n = (math.log(b - a) - math.log(tol)) / math.log(2)
    n_arredondado = round(n)
    print("\nEstimativa de nº de iterações: ", n_arredondado)

    #Verifica as condições de parada para prosseguir com o Método da Bisseção
    while abs(b - a) >= tol:
        pm = (a + b) / 2
        if abs(b - a) < tol:
            break
        elif f(pm) * f(a) < 0:
            b = pm
        else:
            a = pm
        
    return (a + b) / 2, f((a + b) / 2)

#Função
def funcao(x):
    if x <= 0:
        return float('inf') #Retorna infinito para evitar problemas com log na zero ou log negativo
    return x**2 - math.log(x)

ponto_medio, solucao = bissecao(funcao, a, b, tol)
print("A convergência ocorre no ponto médio: ", ponto_medio)
solucao_formatado = "{:.3f}".format(solucao)
print("A solução é: ", solucao_formatado)