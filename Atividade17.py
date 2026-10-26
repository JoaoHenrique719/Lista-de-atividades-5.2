#Se os pontos do jogador forem maiores que 1000, mude a variável nível para 2 e dê um bônus de 100 de vida.

nivel = 1
pontos_nivel = 0
vida = 50

ataque = str(input("Deseja atacar?(s/n)"))

if ataque =="s":
    print("O herói atacou.")
    pontos_nivel += 1000
    
if pontos_nivel >= 1000:
    print("O herói subiu de nível.")
    nivel += 1
    pontos_nivel -= 1000
    
if nivel >= 1:
    print("O herói ganhou 100 de vida")
    vida += 100
