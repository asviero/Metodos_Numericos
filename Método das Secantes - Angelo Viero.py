#Método das Secantes
def secantes(f, x0, x1, tol, max_iter):
    iter_count = 0
    list = []  #Lista
    
    while iter_count < max_iter:
        #Utilizando o método
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        #Adicionando os valores de x0, x1, e a raiz atual à lista
        list.append((x0, x1, x2))
        
        #Verifica se a diferença entre as duas últimas aproximações é menor que a tolerância
        if abs(x2 - x1) < tol:
            return x2, iter_count + 1, list  # Retorna a raiz, o número de iterações realizadas e a lista de valores

        #Atualiza os valores para a próxima iteração
        x0 = x1
        x1 = x2
        iter_count += 1

    #Se o número máximo de iterações for atingido sem convergência, retorna o valor atual de x
    return x2, max_iter, list

#Função
def f(x):
    return x**3 - 2*x - 5

#Parâmetros
x0 = 2.08
x1 = 2.1
tolerance = 0.000001  # Tolerância
max_iterations = 10  # Número máximo de iterações

#Chamando a função do método das secantes
root, iterations, list = secantes(f, x0, x1, tolerance, max_iterations)

#Imprimindo a tabela de valores de x0, x1, e a raiz de cada iteração
print("\nTabela de valores de x0, x1, e a raiz de cada iteração:")
print("Iteração |   x0   |   x1   |   Raiz")
for i, (x0_val, x1_val, root_val) in enumerate(list):
    print(f"{i+1:8d} | {x0_val:.6f} | {x1_val:.6f} | {root_val:.6f}")

print("\nA raiz encontrada é:", root)
print("Número de iterações realizadas:", iterations)