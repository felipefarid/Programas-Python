x = int(input("Digite um numero inteiro para saber o fatorial: "))
contador = 1
while x > 1:
    contador = contador * x 
    x = x - 1

print(contador)