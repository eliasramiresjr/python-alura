from extratorArgumentosUrl import ExtratorArgumentosUrl

# url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

url1 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url1)
argumentosUrl2 = ExtratorArgumentosUrl(url2)

# moedaOrigem, moedaDestino = argumentosUrl.extraiArgumento()
# valor = argumentosUrl.extraiValor()

# print(moedaDestino, moedaOrigem, valor)

# print(argumentosUrl)

print(id(argumentosUrl))
print(id(argumentosUrl2))
print(argumentosUrl==argumentosUrl2)

# "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"