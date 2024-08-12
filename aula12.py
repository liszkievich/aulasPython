nome = 'Carlos Alexandre'
altura = 1.94
peso = 114
imc =  peso / (altura * 2) #É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
resultado = f'{nome} tem {altura} de altura e \npesa {peso} quilos e seu IMC é \n{imc:.2f}'
print(resultado)