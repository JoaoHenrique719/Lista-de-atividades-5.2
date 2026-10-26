# Crie um script que peça a idade do usuário. Se for 18 ou mais exiba exiba "Acesso liberado ao Jogo". Caso contrário, exiba "Acesso Negado".

idade = int(input("Qual a sua idade?"))

if idade < 18:
    print("Você ainda é menor de idade, não pode acessar o jogo.")
    
else:
    print("Acesso Liberado.")
