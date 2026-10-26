# Peça um número ao usuário. Use o operador % e uma estrutra if/else para dizer se o número é par ou ímpar.

valor = int(input("Escolha um número:"))

valor %= 2

if valor == 0:
    print("O número digitado é par.")
    
else: 
    print("O número digitado é ímpar.")
