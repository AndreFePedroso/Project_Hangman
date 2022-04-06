import random
Palavras = ["Teste","Aparelho","Sensor","Favorito","cinza","Bala"]

test = 10
foram = ['']
palavra = random.choice(Palavras)
crip = '_'*len(palavra)
print(palavra)
print('Adivinhe a palavra')
print(crip)

while test > 0 and '_' in crip:
    test -= 1
    l = input('Letra: ')
    if l in palavra and l not in foram :
        local = palavra.find(l)
        crip = crip[:local]+l+crip[local+1:]
        print(crip)
        foram.append(l)
        print(f'voce ainda possui {test} chances')
    else:
        l = input("Tente outra vez: ")
        print(crip)