# Peça ao usuário dois números (m1 e n2). O programa deve digitar uma senha e use um if para verificar se ele acertou.

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))

if n1 > n2:
    print("O primeiro valor é maior que o segundo.")
    
elif n1 < n2:
    print("O segundo valor é maior que o primeiro.")
    
else:
    print("O valores são iguais.")
