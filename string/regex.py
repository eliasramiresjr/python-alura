import re

email1 = "Meu numero é 912341234"
email2 = "Fale comigo em 81234-1234 esse é meu telefone"
email3 = "71234-1234 é o meu celular"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email1)
print(retorno)