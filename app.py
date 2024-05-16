player = {
    "Nome": "",
    "Classe": ""
}
magoClasse = {
    "Classe": "Mago",
    "Arma": "Cajado"
}
cavaleiroClasse = {
    "Classe": "Cavaleiro",
    "Arma": "Espada"
}
arqueiroClasse = {
    "Classe": "Arqueiro",
    "Arma": "Arco"
}

while True:
    player["Nome"] = input("Digite seu nome: ")
    print("Escolha um Classe: \n 1: Mago \n 2: Cavaleiro \n 3: Arqueiro")
    player["Classe"] = int (input())

    if player["Classe"] == 1:
        print("Nome: ",player["Nome"])
        print(magoClasse)
        break
    elif player["Classe"] == 2:
        print("Nome: ",player["Nome"])
        print(cavaleiroClasse)
        break
    elif player["Classe"] == 3:
        print("Nome: ",player["Nome"])
        print(arqueiroClasse)  
        break 
    else:
        print("Digite algo valido!")

print("\n Bem Vindo ao SophieValle")
print("Escolha uma das opções para continuar: \n")

print("Menu: \n")
print("1: Jogar \n 2: Continuar \n 3: Sair \n ")
menuEscolha = int ( input(": "))

if menuEscolha == 1:
    print("Carregando...")
elif menuEscolha == 2:
    print("Aguarde, recuperando log...")
elif menuEscolha == 3:
    print("Saindo...")
else:
    print("Ação invalida!")






