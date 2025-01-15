import json

faturamento = {
    "dias": [
        {"dia": 1, "valor": 200},
        {"dia": 2, "valor": 0},
        {"dia": 3, "valor": 150},
        {"dia": 4, "valor": 300},
        {"dia": 5, "valor": 0},
        {"dia": 6, "valor": 100}
    ]
}

valores = [dia["valor"] for dia in faturamento["dias"] if dia["valor"] > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima_da_media}")