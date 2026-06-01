#copinha 2026

#Grupo do zapzap
zapzap = []
#Estoque
pacotes = 500
album = [

            {
                "modelo" : "capa mole",
                "valor": 25,
                "quantidade": 20
            },

            {
                "modelo" : "capa dura",
                "valor": 80,
                "quantidade": 20
            },
            {
                "modelo" : "edição luxo premium",
                "valor": 180,
                "quantidade": 20
            }
        ]

while True:
    print('''Olá, seja bem vindo a minha lojinha de figurinhas da copa de 2026.
    Escolha o que deseja:
    1 - Comprar pacotes de figurinhas
    2 - Comprar álbum da copa
    3 - Entrar no grupo de troca de figurinhas
    4 - Sair da loja
          ''')
    desejo = int(input("Digite a opção: "))

    if desejo == 4:
        print("Volte Sempre!!")
        break

    if desejo == 3:
        print("---- Entrar no grupo de troca ----")
        nome = input("Digite o seu nome e sobrenome: ")
        numero = int(input("Digite o seu número do whatsapp: "))
        diccgrupo = {"nome": nome,
            "numero": numero}
        zapzap.append(diccgrupo)
        print("Você foi cadastrado com sucesso. Em breve adicionaremos você no grupo de troca de figurinhas!!")
        print("Já temos", len(zapzap), "pessoas no grupo.")

    if desejo == 1:
        print("--- Comprar pacotes de figurinhas ---")
        quantidade = int(input('''
    O pacote custa R$7,00 Reais.
    Quantas deseja comprar? '''))
        valor = 7*quantidade
        if quantidade <= pacotes:
            print(f'''
    {quantidade} pacotes de figurinhas foram adicionados.
    Valor total foi de R${valor}''')
            pacotes -= quantidade
        elif quantidade > pacotes:
            valor2 = 7*pacotes
            print(f'''
    Desculpa, não temos essa quantidade.
    Só {pacotes} de pacotes foram adicionados, não temos mais estoque.
    Valor total R${valor2}''')

    if desejo == 2:
        print("--- Comprar álbum da copa ---")
        for albuns in album:
           print("Modelo:", albuns ["modelo"])
           print("Valor:", albuns ["valor"])
        escolha = input("Qual modelo deseja comprar? ").lower()
        quant_album = int(input("Quantos álbuns vai comprar? "))

        for albuns in album:
            if escolha == albuns ["modelo"]:
                if quant_album <= albuns["quantidade"]:
                    valor_album = albuns ["valor"]*quant_album
                    albuns["quantidade"] -= quant_album
                    print(f'''
    {quant_album} álbuns do modelo {escolha} foram adicionados no carrinho.
    O valor total foi R${valor_album}''')
                elif quant_album > albuns["quantidade"]:
                    quant_disponivel = albuns["quantidade"]
                    valor2 = quant_disponivel * albuns["valor"]
                    print(f'''
    Só {quant_disponivel} foram adicionados, não temos mais no estoque.
    O Valor total foi R${valor2} ''')
                    albuns["quantidade"] = 0
    else:
        print("opção invalida.")
                    
            
                    

                              
