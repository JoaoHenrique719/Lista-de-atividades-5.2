# Crie um programa que receba a nota de um aluno:
#- Se for 7 ou mais: "aprovado"
# Se for entre 5 e 6.9: "recuperação"
# Se for menor que 5: "Reprovado"

nota = float(input("Digite a nota do aluno:"))

if nota > 6.9:
    print("Aprovado.")
    
elif nota > 4.9:
    print("Recuperação.")
    
else:
    print("Reprovado.")
