nome = 'Luiz Otávio'
indice = 0
nova_string = ''

while indice < len(nome):
    nova_string = nova_string+nome[indice]+'*'
    indice += 1
print (nova_string)