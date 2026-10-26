#Crie um menu onde o jogador escolhe entre 1 (falar), 2(atacar) ou (fugir). Use if/elif/else para exibir uma resposta diferente para cada escolha.
heroi = True
print(" -------")
print("|1.falar |")
print("|2.atacar|")
print("|3.fugir |")
print(" -------")

while heroi == True: 
    acao = int(input("Qual a ação do herói?"))

    if acao == 1:
        print("O herói olha pra uma parede e começa a falar sozinho, talvez ele esteja praticando pra falar com o rei.")
    
    elif acao == 2:
        print("O herói saca a espada e golpeia o ar, ele deve ter achado um inimigo invisível.")
    
    elif acao == 3:
        print("O herói gira 180° graus, e sai correndo, ele deve ter partido pra uma aventura.")
        heroi = False
    
    
    else:
        print("O herói continua parado, deve ter pensando qual o seu próximo passo.")
