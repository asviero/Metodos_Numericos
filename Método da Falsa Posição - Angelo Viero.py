import math

<<<<<<< HEAD
#Método da Falsa Posicão
def false_position(funcao, a, b, tol, max_iter):
    tabela = []

=======
def falsa_posicao(funcao, a, b, tol, max_iter):
    tabela = []  #Lista para armazenar os valores de x e f(x)
>>>>>>> daaf1836b279cea51f34c717a6a8bed91a1daa59
    for i in range(max_iter):
        #Adicionando os valores atuais à tabela
        tabela.append([a, b, funcao(a), funcao(b)])
        
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        #Adiciona os valores de x e f(x) na tabela
        tabela.append((x, funcao(x)))
        
        #Critério de parada
        if abs(funcao(x)) < tol:
<<<<<<< HEAD
            return x, funcao(x), tabela
=======
            return tabela
>>>>>>> daaf1836b279cea51f34c717a6a8bed91a1daa59
        
        #Atualizando o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.")

def funcao(x):
<<<<<<< HEAD
    return math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6 #math.exp(-x) seria e^x

estimativa_raiz, funcao_valor, tabela = false_position(funcao, a=1.82, b=1.84, tol=0.001, max_iter=50)

#Tabela
print("\nTabela de iterações:")
print("a\t| b\t| valor de f(a)\t| valor de f(b)")
print("-" * 50)
for linha in tabela:
    print("\t|".join(map(str, linha)))
=======
    #return 2.718281**x + 2**(-x) + 2 * math.cos(x) - 6
    return 4 * math.cos(x) - 2.718281**(2 * x)

tabela = falsa_posicao(funcao, a = 0.5, b = 0.6, tol = 0.001, max_iter = 20)

#Tabela
print("\tx\tf(x)")
print("-" * 25)
for x, fx in tabela:
    print("{:.6f}\t{:.6f}".format(x, fx))
>>>>>>> daaf1836b279cea51f34c717a6a8bed91a1daa59
