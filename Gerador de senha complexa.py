#Introdução ao gerador de senha
#gerar numeros aleatórios
#gerar caracters aleatórios
#gerar letras aelatórias
#gerar baseado no tamanho da senha que o usuário quer

import random 


x = int(input("qual o tamanho da senha que quer? (max 15): "))


thislist = ["a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","w","z"]
thislist2 = ["!","@","#","$","%","¨&","*","(",")"]
a = random.randrange(0,10,1)
b = random.randrange(0,10,1)
c = random.randrange(0,10,1)
d = random.randrange(0,10,1)
e = random.choice(thislist2)
f = random.randrange(0,10,1)
g = random.randrange(0,10,1)
h = random.choice(thislist)
i = random.choice(thislist)
j = random.choice(thislist)
k = random.choice(thislist)
l = random.choice(thislist)
m = random.choice(thislist2)
n = random.choice(thislist2)
o = random.choice(thislist2)

itens = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
random.shuffle(itens)
y = random.sample(itens, x)

for u in y:
 print(u, end='' )


 



