#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

numeros_alunos = 10
medias = []
aprovados = 0

for i in range(numeros_alunos): #loop que percorre cada aluno
    notas = []

    for j in range(4): #loop que pede as quatro notas do aluno
        nota = float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
        notas.append(nota)

    media = sum(notas) / len(notas) #calcula a média das notas do aluno
    medias.append(media)  #adiciona a média à lista de médias

    if media >= 7:
        aprovados += 1 

print(f'Número de alunos aprovados: {aprovados}')

