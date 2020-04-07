n = int(input("Digite um numero para ver seu resultado fatorial: "))
def fatorial (n):
    if n == 1:
      return n
    return fatorial (n-1) * n
    
print(fatorial(n))