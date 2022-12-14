# Aula 03 - B - 2022/11/09 

# Exemplos de Funções

print("Início da Aula 03 - B - (09/11/2023)\n")

# Criação de funções

preco = 1999.90

# Calcular apenas 5% de imposto, guardar na variável imposto e exibir na tela 
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função calcular_imposto() que calcula um imposto de 5% e retorno à quem pediu... 
# Isso é a declaração da função (Como ele funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

# Aqui é o uso... Aqui é imposto a calcular..
preco = 299
imposto = calcular_imposto(preco)
print(imposto)
print(f"\nEsse aqui é com a função (7%): {imposto}")

# Explicação de variável local x global
print(preco) #???
preco_produto = 100
print(preco_produto) #???

# Agora calcular imposto a aliquota é 7% 
valores = [1.99, 24.50, 78.27, 1515.5]
# Se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de ... é ..." (1o. preço, 2o. imposto)

# Forma 01 
print("\n")
for valor in valores:
      imposto = calcular_imposto(valor)
      print(imposto)
  
print("\nImposto de 7%\n")
# Forma 02
for valor in valores :
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")
print("\n")

#Declarar uma função calcular_imposto_aliquota() que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada, e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

print("\n")
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

print("\nImposto de 10%\n")
# E se agora o imposto for 10%? 
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")


