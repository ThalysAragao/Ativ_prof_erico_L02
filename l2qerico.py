#cria uma lista

#entrada
def cria_lista (numero):
    for nl in range(numero + 1):
        for nc in range (nl):
            print (f'{nl:4}',end= ' ')
        print ()
numero = int (input('digite: '))
cria_lista (numero)