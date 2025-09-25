#1 - 

Tel = input("Digite o número de telefone, com o codigo do país e o DDD (somente os numeros): ")

Inv = "Número de telefone inválido."

if ((Tel[0:2] != "55") #validação código brasileiro 
    or ((len(Tel) != 12) and (len(Tel) != 13)) #validação número de dígitos 
    or ((len(Tel) == 13) and (int(Tel[4:9]) < 91000 or int(Tel[4:9]) > 99999)) #validação celular
    or ((len(Tel) == 12) and (int(Tel[4:8]) < 2000 or int(Tel[4:8]) > 5999)) #validação fixo
    or ((int(Tel[2:4]) < 11) or (int(Tel[2:4]) > 99) )): #validação ddd
    print(Inv)
else: 
    if ((len(Tel) == 12)):
        TelFormat = "+" + Tel[0:2] + " " + Tel[2:4] + " " + Tel[4:8] + "-" + Tel[8:]
        print(TelFormat)
    else:
        TelFormat = "+" + Tel[0:2] + " " + Tel[2:4] + " " + Tel[4:9] + "-" + Tel[9:]
        print(TelFormat)

#2 - 

Med = 0.0
Aprov = "Reprovado."

while True:
    try:
        NumNotas = int(input("Digite o número de notas que farão parte da média: "))

        if NumNotas < 0:
            raise ValueError("Favor digitar um número positivo")
        
        break

    except ValueError as e:
        print("\nErro: {}\n".format(e))

for x in range(0, NumNotas):
    while True:
        try:
            Nota = float(input("Digite a {}° nota: ".format(x + 1)))

            if Nota < 0 or Nota > 10:
                raise ValueError("Favor digitar uma nota entre 0 e 10.")
            
            Med += Nota
            break

        except ValueError as e:
            print("\nErro: {}\n".format(e))


Med = Med / NumNotas

if Med >= 6:
    Aprov = "Aprovado."

print("\nMédia: {}. {}".format(Med, Aprov))

#3 - 

while True: 
    try:
        Dec = int(input("Digite um número inteiro decimal: "))
        break
    except ValueError:
        print("Erro: Digite um valor válido.\n")


while True:
    Menu = input("Escolha para qual base numérica será feita a conversão: \n\n(1) - Binário \n(2) - Octal \n(3) - Hexadecimal\n\n")

    if Menu == "1":
        Bin = bin(Dec)
        print("Em binário: {}".format(Bin))
        break
    elif Menu == "2":
        Oct = oct(Dec)
        print("Em octal: {}".format(Oct))
        break
    elif Menu == "3":
        Hex = hex(Dec)
        print("Em hexadecimal: {}".format(Hex))
        break
    else:
        print("\nValor inválido.\n")

#4 - 

W_List = []
Err = "Valor inválido. Digite novamente."

while True:
    try:        
        W_Index = int(input("Digite o número de palavras da lista: "))

        if W_Index < 0:
            print(Err)
        else:
            break
    except ValueError:
        print(Err)

for x in range(0, W_Index):
    W = input(f"Digite a {x + 1}° palavra: ")
    W_List.append(W)


for x in range(0, W_Index):
    W1 = sorted(W_List[x])

    for y in range(0, W_Index):
        if y != x:
            W2 = sorted(W_List[y])

            if W1 == W2:
                print(f"{W_List[x]} e {W_List[y]} são anagramas.")

#5 - 

stock = []

while True:
    int_menu = input("Escolha uma dentre as opções (1, 2, 3, 4 ou 5): \n\n1 - Criar \n2 - Ler \n3 - Atualizar \n4 - Deletar \n5 - Encerrar\n\n")

    if int_menu == "1":
        product = input("\nDigite o nome do produto a ser adicionado: ")
        stock.append(product)

    elif int_menu == "2":
        print("")
        print(stock)
        print("")
    
    elif int_menu == "3":
        remove = input("\nDigite o nome do produto que deseja atualizar: ")

        if remove in stock:
            new = input("\nInsira o nome do produto atualizado: ")
            stock.remove(remove)
            stock.append(new)

        else:
            print("\n\nproduto não encontrado\n")

    elif int_menu == "4":
        remove = input("\nDigite o nome do produto que deseja remover: ")
        
        if remove in stock:
            stock.remove(remove)

        else:
            print("\n\nproduto não encontrado\n")

    
    elif int_menu == "5":
        print("\nEncerrando programa.")
        break
    else:
        print("\n\nOpção inválida.\n\n")

#6 - 

import string
import random

character_list = string.ascii_letters + string.digits + string.punctuation
password = ""

while True:
    try:
        length = int(input("Digite o tamanho da senha (min. 8): "))

        if length < 8:
            print("Senha muito curta.")
        else:
            break
    except ValueError:
        print("Valor inválido.")

for x in range(length):
    password += random.choice(character_list)

print(password)