nome = input("Digite seu nome: ")
encontrar = input("Qual letra ou palavra deseja encontrar no nome?: ")

if encontrar in nome:
    print(f"{encontrar} esta em {nome}")
else:
    print("Nao existe!")