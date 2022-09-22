# Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e apresentar:

# a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;

# b) A mensagem"Reprovado", se a média for menor do que 7, com a respectiva média alcançada;

# c) A mensagem "Aprovado com Distinção", se a média for igual a 10.


nome = input("Qual seu nome? ")
print(f"Vamos lá {nome}!")
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))
media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"Parabéns {nome}, você foi aprovado com média {media:.1f}!")

if media < 7:
    print(f"Foi por pouco {nome}, você foi reprovado com média {media:.1f}:(")

if media == 10:
    print(f"Parabéns {nome}, você foi aprovado com distinção!")