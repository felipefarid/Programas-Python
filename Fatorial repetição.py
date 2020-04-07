x = int(input("Digite um numero inteiro positivo para saber o fatorial: "))


while x >= 0: 
    f = 1
    while x > 1:
        f = f * x
        x = x - 1
    print(f)
    x = int(input("Digite um numero inteiro positivo para saber o fatorial: "))       