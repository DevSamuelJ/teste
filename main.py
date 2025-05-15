soma = 0
qntNumeros = int(input("Digite quantos numeros você deseja somar: "))
for i in range(1,qntNumeros+1):
    numero = int(input(f"Digite o {i}º numero: "))
    soma+=numero

print(f"A soma de todos os numeros é {soma}")