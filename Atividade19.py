#O jogador quer pegar um item de peso 5. Verifique se o peso_atual + 5 ultrapassa o limite_maximo de 50. Se o ultrapassar, imprima "inventário Cheio"

peso_atual = 45
ouro = 5
heroi = True

while heroi == True:
    print(f"O herói achou uma pepita de ouro bruto, a pepita pesa {ouro}, o herói possui {peso_atual} de peso, com 50 ele fica com o inventário cheio.\
        Qual a ação do herói?")
    
    print(" -------")
    print("|1.pegar |")
    print("|2.deixar|")
    print(" -------")
    
    acao = int(input("Qual a ação do herói?"))
    
    
    if peso_atual >= 50 and acao == 1:
            print("O herói já chegou ao peso limite.")
            
    elif acao == 1:
        peso_atual += ouro
        print(f"O herói pegou a pepita e está com {peso_atual} de peso.")
        
    
    elif acao == 2:
        print("O herói deixou a pepita para átras e foi embora.")
        heroi = False
        
    else:
        print("O herói ainda não se decidiu.")
