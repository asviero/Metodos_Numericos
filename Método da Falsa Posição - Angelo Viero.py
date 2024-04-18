import math

#Método da Falsa Posicão
def false_position(funcao, a, b, tol, max_iter):
    tabela = []

    for i in range(max_iter):
        #Adicionando os valores atuais à tabela
        tabela.append([a, b, funcao(a), funcao(b)])
        
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        #Adiciona os valores de x e f(x) na tabela
        tabela.append((x, funcao(x)))
        
        #Critério de parada
        if abs(funcao(x)) < tol:
            return x, funcao(x), tabela
        
        #Atualizando o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.")

def funcao(x):
    return math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6 #math.exp(-x) seria e^x

estimativa_raiz, funcao_valor, tabela = false_position(funcao, a=1.82, b=1.84, tol=0.001, max_iter=50)

#Tabela
print("\nTabela de iterações:")
print("a\t| b\t| valor de f(a)\t| valor de f(b)")
print("-" * 50)
for linha in tabela:
    print("\t|".join(map(str, linha)))
