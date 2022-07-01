nome = []

sobrenome = []

numeronomes = int(input("Insira a quantidade de nomes e sobrenomes: "))

for i in range(numeronomes):
	nome1 = str(input("Insira os nomes e sobrenomes: ")).split(" ")
	nome.append(nome1[0])
	sobrenome.append(nome1[1])

nome.sort()
sobrenome.sort()

for l, r in enumerate(nome):
	print (f"{r} {sobrenome[l]}")
