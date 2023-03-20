'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
a, e, i, o, u'''
palavra = input('Digite uma letra: ').lower()
vogais = ('a','e','i','o','u')
if palavra in vogais:
    print("É uma vogal")
else:
    print('É uma consoante')