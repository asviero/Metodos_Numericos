#Método das Secantes
def secant_method(f, x0, x1, tol, max_iter):
    iter_count = 0
    while iter_count < max_iter:
        #Utilizando o método
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        #Verifica se a diferença entre as duas últimas aproximações é menor que a tolerância
        if abs(x2 - x1) < tol:
            return x2, iter_count + 1  # Retorna a raiz e o número de iterações realizadas

        #Atualiza os valores para a próxima iteração
        x0 = x1
        x1 = x2
        iter_count += 1

    #Se o número máximo de iterações for atingido sem convergência, retorna o valor atual de x
    return x2, max_iter


#Função
def f(x):
    return x**3 - 2*x - 5

#Parâmetros
x0 = 2  # Primeiro ponto inicial
x1 = 3  # Segundo ponto inicial
tolerance = 1e-6  # Tolerância
max_iterations = 1000  # Número máximo de iterações

# Chamando a função do método das secantes
root, iterations = secant_method(f, x0, x1, tolerance, max_iterations)

print("A raiz encontrada é:", root)
print("Número de iterações realizadas:", iterations)
