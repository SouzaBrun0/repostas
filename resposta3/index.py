import json

# Carregar os dados de faturamento a partir de um arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

# Extrair os valores de faturamento, ignorando dias sem faturamento (valor 0)
faturamento = [dia['valor'] for dia in data['faturamento'] if dia['valor'] > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor}")
print(f"Maior valor de faturamento: R${maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
