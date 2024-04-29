import math

#Método da Falsa Posicão
def false_position(funcao, a, b, tol, max_iter):
    tabela = [("Iteração", "a", "b", "f(a)", "f(b)")]

    for i in range(max_iter):
        
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        # Adicionando os valores à tabela
        tabela.append((i+1, a, b, funcao(a), funcao(b)))
        
        # Critério de parada
        if abs(funcao(x)) < tol:
            return x, funcao(x), tabela
        
        #Atualizando o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.")

def funcao(x):
    return math.exp(-x) + 2**(-x) + 2 * math.cos(x) - 6 #math.exp(-x) seria e^x

estimativa_raiz, funcao_valor, tabela = false_position(funcao, a=1.82, b=1.84, tol=0.001, max_iter=50)

#Tabela
for linha in tabela:
    if linha[0] == "Iteração":
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*linha))
        print("-" * 50)
    else:
        print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(*linha))
        print("-" * 50)
