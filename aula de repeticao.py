#aula_lacos_repeticao.py
#lacos de repeticao
# Usando o laco while

contador = 0

while contador < 3:
    print('valor',contador)
    contador = contador + 1


    print('acabou')
    #Exercicio: faca um laco de repeticao while que mostra os valores de 08 a 12

    
    valor = 0

    while valor <=12:
        print('valor',valor)
        valor = valor +1


    #Exercicio: faca um laco de repeticao while que mostra os valores de 19 a 14
    
u = 19

while u >= 14:
    print('valor de u: ', u)
    u = u - 1

# laco de repeticao FOR o mais top de todos
print('Usando laco FOR')

for b in range(5):
    print('usando de Z', b)


#Exercicio:Usando o for, mostre todos os valores pares entre 0 e 10

for b in range(11):
    if b % 2 == 0:
       print(b,'epar ')