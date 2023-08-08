def calcular_fatorial(variavel):
    fatorial_calculado = 1
    while (variavel>0):
        fatorial_calculado = fatorial_calculado * variavel
        variavel = variavel - 1

    return fatorial_calculado


print("Esse programa calculará o fatorial de um número.")
print("------------------------------------------------")
print("Vamos começar agora.")
print("------------------------------------------------")
print("------------------------------------------------")
repete ="1"
while (repete=="1"):
    numero = int(input("Por favor, digite o número:"))
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é igual a {fatorial}")
    repete = input("Deseja calcular o fatorial de outro número? (1 para sim, qualquer tecla para sair): ")
else:
    print("Fim da execução")