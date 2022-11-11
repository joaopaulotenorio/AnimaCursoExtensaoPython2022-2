# Aula 02 - A - 2022/10/26 

print("Início da aula 02 - A - (26/10/2022)\n")

# Comando input(): quero permitir que 
# O usuário digite algo...
nome = input("Digite seu nome: ")

# Pede a idade para o usuário "Qual sua idade?"
idade1 = input("Digite sua idade: ")
idade = int(input("Digite sua idade: "))

# Comando de saída... exibir na tela
print(f"Boa noite! Seu nome é {nome}")
# Exiba "Sua idade é ..."
print("E sua idade é {}".format(idade))

# E se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

dobro1 = idade1 * 2
print("O dobro da idade informada é {}".format(dobro1))

# Estrutura condicional - o famoso "SE" (if)
# Se a pessoa for maior de idade, mostre "Você é maio de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")
else:
  print("Você é xóven ainda, xóven ainda...")

# E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
# Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe o gênero M-Masculno || F-Feminino || O-Outros: ")
if idade >=18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório.")




print("Vai ser executada de qualquer jeito")

