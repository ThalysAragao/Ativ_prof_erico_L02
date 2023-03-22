'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input('Digite seu turno, M - matutino, V - vespertino, N - noturno: ').upper()

if turno == "M":
    print("bom dia!")
elif turno == "V":
    print("boa tarde!")
elif turno == "N":
    print("boa noite!")
else:
    print("valor inválido!")