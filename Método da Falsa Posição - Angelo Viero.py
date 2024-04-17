import math

'''
a = float(input("Selecione o ponto a: "))
b = float(input("Selecione o ponto b: "))
tol = float(input("Selecione a tolerância: "))
max_iter = float(input("Selecione a máxima iteração: "))
'''

def false_position(funcao, a, b, tol, max_iter):

    for i in range(max_iter):
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        #Critério de parada
        if abs(funcao(x)) < tol:
            return x, funcao(x)
        
        #Atualiza o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.".format(max_iter))

def funcao(x):
    return 2.71828**x + 2**(-x) + 2 * math.cos(x) - 6 #em vez de colocar 'e' elevado na x, coloquei diretamente o valor do número de Euler

estimativa_raiz, funcao_valor = false_position(funcao, a = 1.82, b = (1.84), tol = 0.001, max_iter = 50)
print("Estimativa da raiz:", estimativa_raiz)
print("Valor de f(x) = ", funcao_valor)