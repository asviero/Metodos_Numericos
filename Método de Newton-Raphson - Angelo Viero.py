import math

#Método de Newton-Raphson
def newton_raphson(funcao, derivada, x0, tol, max_iter):
    tabela = []  #Lista vazia
    x_antigo = x0
    for i in range(max_iter):
        x_atual = x_antigo - (funcao(x_antigo) / derivada(x_antigo))
        primeiro_criterio = abs(x_atual - x_antigo) / abs(x_atual)
        segundo_criterio = abs(funcao(x_atual))

        tabela.append([i, x_antigo, funcao(x_antigo), derivada(x_antigo), primeiro_criterio, segundo_criterio])

        #Critério de parada 1
        if primeiro_criterio < tol:
            print("\nRaiz saiu pelo domínio. (Primeiro critério de parada)")
            return x_atual, tabela

        #Critério de parada 2
        if segundo_criterio < tol:
            print("\nRaiz saiu pela raiz. (Segundo critério de parada)")
            return x_atual, tabela
        #Atualiza o valor de x
        x_antigo = x_atual

    raise ValueError("Atingiu o número máximo de iterações.")

def funcao(x):
    return 3 * x - math.exp(-x)  #math.exp(-x) seria e^-x

def derivada(x):
    return 3 + math.exp(-x)

#Chamada da função
x0 = 1.5
raiz, tabela = newton_raphson(funcao, derivada, x0, tol=0.0001, max_iter=10)

print("Raiz encontrada:", raiz)

#Tabela
print("\nTabela de iterações:")
print("{:<10} | {:<20} | {:<20} | {:<20} | {:<20} | {:<20}".format("Iteração", "x", "Função", "Derivada", "Primeiro Critério", "Segundo Critério"))
print("-" * 121)
for linha in tabela:
    print("{:<10} | {:<20.10f} | {:<20.10f} | {:<20.10f} | {:<20.10f} | {:<20.10f}".format(*linha))
