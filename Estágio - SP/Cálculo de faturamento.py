import json

# Dados de faturamento
faturamento_diario = {
    "01": 1000,
    "02": 1500,
    "03": 2000,
    "04": 0,
    "05": 0,
    "06": 3000,
    "07": 3500,
    "08": 0,
    "09": 4000,
    "10": 0,
    "11": 2500,
    "12": 5000,
    "13": 6000,
    "14": 0,
}

# Cálculo
valores = [v for v in faturamento_diario.values() if v > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_media = sum(1 for v in valores if v > media_mensal)

# Resultados
print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
