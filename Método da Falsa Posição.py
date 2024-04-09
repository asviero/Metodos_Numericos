import math

'''
a = float(input("Selecione o ponto a: "))
b = float(input("Selecione o ponto b: "))
tol = float(input("Selecione a tolerância: "))
max_iter = float(input("Selecione a máxima iteração: "))
'''

def false_position(funcao, a, b, tol, max_iter):

    #Condição do método: "a" e "b" precisam ter sinais opostos
    if funcao(a) * funcao(b) >= 0:
        raise ValueError("Os valores de f(a) e f(b) têm o mesmo sinal.")
    
    for i in range(max_iter):
        #Método da Falsa Posição
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        #Critério de parada
        if abs(funcao(x)) < tol:
            return x #, funcao(x)
        
        #Atualiza o intervalo [a, b]
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError("O método não convergiu após o número máximo de iterações.".format(max_iter))

def funcao(x):
    return (4 * math.cos(x)) - 2.71828**(2 * x) #em vez de colocar e**(2 * x), coloquei diretamente o valor do número de Euler

#Caso queira printar o valor de f(x), acrescentar funcao_valor na linha abaixo
estimativa_raiz = false_position(funcao, a = 0, b = (math.pi / 2), tol = 0.001, max_iter = 50)
print("Estimativa da raiz:", estimativa_raiz)
#print("Valor de f(x) = ", funcao_valor)