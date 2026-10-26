#Crie uma variável senha_mestra = "python123". Peça ao usuário para digitar uma senha e use um if para verificar se ele acertou.

senha_mestra = "python123"
tentativa = True
while tentativa == True:
    senha = input("Qual a senha mestra?")
    
    if senha != senha_mestra:
        print("Senha incorreta.")

    else:
        print("Senha correta.")
        tentativa = False
