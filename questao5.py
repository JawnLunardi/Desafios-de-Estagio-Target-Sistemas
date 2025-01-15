def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

# Entrada
texto = input("Digite uma string: ")
print("String invertida:", inverter_string(texto))