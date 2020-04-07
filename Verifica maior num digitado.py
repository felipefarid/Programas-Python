
entrada = input("digite quantos numeros quiser para saber o maior separados por espaço: ")
split = entrada.split(" ")
numeros = [int(x) for x in split]


print(max(numeros))
