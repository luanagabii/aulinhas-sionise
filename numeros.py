#criar um programa que leia 3 numeros, em seguida o usuario escohe entre:
# 1 - somar os numero
# 2 - colocar em ordem crescente
# 3 - verificar quais sao pares e impares
# 4 - informar o dobro e a metade dos numeros

pares = []
impares = []
numeros = []

def somar_numero ():
    operacao = n1 + n2 + n3
    print (f'''{n1} + {n2} + {n3} = {operacao}
Resultado da soma foi de: {operacao}.''')


def ordem_crescente ():
    numeros.sort()
    print(f"Em ordem crescente ficou: {numeros}")

def pares_impares ():
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print(f'''
          Os números pares são: {pares}.
          Os números impares são: {impares}.''')
    
def dobro_metade():
    dobro1 = n1 * 2
    metade1 = n1 / 2
    print(f'''O dobro de {n1} é : {dobro1}
A metade de {n1} é : {metade1}''')
    print()
    dobro2 = n2 * 2
    metade2 = n2 / 2
    print(f'''O dobro de {n2} é : {dobro2}
A metade de {n2} é : {metade2}''')
    print()
    dobro3 = n3 * 2
    metade3 = n3 / 2
    print(f'''O dobro de {n3} é : {dobro3}
A metade de {n3} é : {metade3}''')
    print()

def sair():
    print("Fechando programa.")



n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)

while True:
    print('''
        1 - Somar os números
        2 - Colocar os números em ordem crescente
        3 - Verificar quais números são pares e impares
        4 - Informar o dobro e a metade dos números
        5 - Sair
            ''')
    desejo = int(input("O que voce deseja? :"))


    if desejo == 1:
        somar_numero()
    if desejo == 2:
        ordem_crescente()
    if desejo == 3:
        pares_impares()
    if desejo == 4:
        dobro_metade()
    if desejo == 5:
        sair()
        break
