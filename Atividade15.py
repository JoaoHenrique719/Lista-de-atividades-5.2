#Crie duas variáveis: tem_chave (booleana) e distância_porta(inteiro).
# O código só deve imprimir "Porta Aberta" se o jogador tiver a chave E a distância menor que 2.

tem_chave = False
distancia_porta = 5
porta_aberta = False

while porta_aberta == False:
    if tem_chave == False:
     pegar_chave = str(input("Você não possui a chave, deseja pegá-la?(sim/nao)"))
    if pegar_chave == "sim":
            print("Você pegou a chave!")
            tem_chave = True
        
    if distancia_porta > 2:
        andar = str(input("Você ainda está muito longe da porta, deseja se aproximar?(sim/nao)"))
        if andar == "sim":
            print("Você andou e se aproximou da porta!")
            distancia_porta -= 3
            
    if distancia_porta >= 2 and tem_chave == True:
        print("Você abriu a porta.")
        porta_aberta = True
