#aula_listas.py

#iniciando uma lista vazia
listaVazia = []
print('lista vazia', ValueError)

#iniciando uma lista de valores inteiros
listaInteiros = [2,4,5,6,9]
print('Lista de Inteiros:,'listaInteiros)

#iniciando uma lista de valores reais
listaReais = [9.8,6.5,2.1,3.02,7.7]
print('lista de reais:',listaReais)

#iniciando uma lista de valores string
listafrutas = ['abacaxi','cupu','ameixa']
print('lista de frutas:',listafrutas)

# adicionando valores lista usado append
listafrutas.append('araca')
print('lista de frutas:',listafrutas)
listafrutas. append('camo_camo')
print('lista de frutas:', listafrutas)

#para sabemos o tamanho dessa lista usndo o lenght de forma abreviada lem
tamanholistafrutas = lem(listafrutas)
print('A lista de fruta possui:>',tamanholistafrutas)

#mostra um valor especifico
print(listafrutas[3])

#Alterar valor da lista com indice espercifico
listafrutas[2]='sapota'
print(listafrutas)

#Excluindo um valor da lista
del listafrutas[4]
print(listafrutas)

















listafrutas[5]