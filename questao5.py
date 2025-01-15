def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string: ")
print("String invertida:", inverter_string(texto))