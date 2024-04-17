import math

def falsa_posicao(funcao, a, b, tol, max_iter):
    tabela = []  #Lista para armazenar os valores de x e f(x)
    for i in range(max_iter):
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        #Adiciona os valores de x e f(x) na tabela
        tabela.append((x, funcao(x)))
        
        #Critério de parada
        if abs(funcao(x)) < tol:
            return tabela
        
        #Atualiza o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.")

def funcao(x):
    #return 2.718281**x + 2**(-x) + 2 * math.cos(x) - 6
    return 4 * math.cos(x) - 2.718281**(2 * x)

tabela = falsa_posicao(funcao, a = 0.5, b = 0.6, tol = 0.001, max_iter = 20)

#Tabela
print("\tx\tf(x)")
print("-" * 25)
for x, fx in tabela:
    print("{:.6f}\t{:.6f}".format(x, fx))