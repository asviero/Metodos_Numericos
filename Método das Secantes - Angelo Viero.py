#Método das Secantes
<<<<<<< HEAD
def secantes(f, x0, x1, tol = 0.00001, max_iter = 100):
=======
def secantes(f, x0, x1, tol, max_iter):
>>>>>>> 0c1734c8aa45256352a04feb20f013d4e5af7d88
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
x0 = 2.08
x1 = 2.1
tolerance = 0.000001  # Tolerância
max_iterations = 10  # Número máximo de iterações

# Chamando a função do método das secantes
root, iterations = secantes(f, x0, x1, tolerance, max_iterations)

print("A raiz encontrada é:", root)
print("Número de iterações realizadas:", iterations)
