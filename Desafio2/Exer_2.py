# 2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o seu turno (M-matutino, V-Vespertino ou N-Noturno): ")   

if turno == "M":
    print("Bom Dia!")

elif turno == "V":
    print("Boa Tarde!")

elif turno == "N":
    print("Boa Noite!")

elif turno != "M" "V" "N" :
    print("Valor Inválido!")
