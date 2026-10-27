#No godot, queremos evitar que o personagem saia da tela. Se a posição_x for menor que 0 ou maior que 1024, imprima "atenção: Saindo da tela!".
Godot = True
x = 512

while Godot == True:
    print(f"A posição de Godot é de {x}, ele não pode sair da sua visão (ultrapassando 0 ou 1024), não deixe que isso aconteça.")

    x = int(input("Me diga, para aonde o Godot devia ir?"))

    if x < 0 or x >  1024:
        print("O Godot está finalmente livre de sua prisão, ele pode voltar para a sua família.")
        Godot = False
