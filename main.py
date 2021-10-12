from extrator_url import ExtratorURL

# extrator_url = ExtratorURL("   ")
# extrator_url = ExtratorURL(None)

# extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(f'Valor do Parâmetro: {valor_quantidade}')
# print(f'Tamanho da URL: {len(extrator_url)}')
# print(extrator_url)

# extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
# extrator_url2 = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
# print(extrator_url == extrator_url2)


# Teste Desafio
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_convertido = int(quantidade) / VALOR_DOLAR
    print(f'Valor convertido em {valor_convertido} em dolares')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_convertido = int(quantidade) * VALOR_DOLAR
    print(f'Valor convertido em {valor_convertido} em reais')
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")