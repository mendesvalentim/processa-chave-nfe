#coding: utf8
from estados import uf


chave = raw_input('Insira a Chave de Aceso: ')
estado = chave[0:2]
resultado = uf(estado)
print estado, resultado

data = chave[2:6]
print data, 'Ano/Mes'

cnpj = chave[6:20]
print cnpj, 'CNPJ'

modelo = chave[20:22]
if modelo=='55':
    print modelo, 'Nf-e'
elif modelo=='65':
    print modelo, 'Nfc-e'

serie = chave[22:25]
print serie, 'Serie'

numero = chave[25:34]
print numero, 'Numero da nota'

contribuinte = chave[34:43]
print contribuinte, 'Numero a ser utilizado pelo emissor da nota fiscal'

print chave[-1], 'Digito'
 







