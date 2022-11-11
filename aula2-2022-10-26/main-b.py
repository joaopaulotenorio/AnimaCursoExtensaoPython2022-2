# Aula 02 - B - 2022/10/26 

# Estrutura condicional

print("Início da aula 02 - B - (26/10/2022)\n")

# Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome}, você é bichão, mesmo..."
nome = input("Informe o seu nome: ")
nota = float(input("Digite a sua nota: "))

if (nota == 10):
  print(f"{nome}, você é bichão, mesmo...")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho!")
else:
  print("Burro, não tirou nem seis...")


