# Aula 03 - A - 2022/11/09 

# Exemplos de laços (Loops) e Listas (while e for)

print("Início da aula (09/11/2023)")

contador = 1

# Exibir de 1 até 10 repetidamente

while(contador <= 1000):
  print(contador)
  contador = contador+1 #contador +=1
print("\nLaços for e while \n")
  
# Laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

# Lista
frutas = ["morango", "laranja", "pêra"]

# mostra todas
print(frutas)
# quero exibir a 3a. fruta (pêra)
print(frutas[2])

print(frutas[1]) # 
print(frutas[0]) #

# Exibir quantas frutas tem na minha lista?
print(len(frutas)) # length = tamanho

# Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas))
print(frutas)

print(frutas[0]) # 

print("\nExemplo das frutas com while..\n")
frutas.append("uva")

# Imprimir a lista de frutas uma a uma ate o tamanho
i = 0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("\nExemplo das frutas com for..\n")
for fruta in frutas :
  print(fruta)

