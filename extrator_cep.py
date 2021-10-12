import re

endereco = "Rua Professor Teodorico, 815, Apto 202 - Montese, Fortaleza-CE, 60410-343"
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
print(cep)