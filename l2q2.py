"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
#entrada

numero = int(input('Digite um numero: '))

#processamento e saida

if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O numero é negativo')