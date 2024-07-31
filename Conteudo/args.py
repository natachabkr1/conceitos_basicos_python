# args e kwargs

# kwargs (nomeia a função) **
def mini_bio(**dados_pessoais):
    for key,value in dados_pessoais.items():
        print(f'{key} {value}')
        print('###Mini biografia###')
mini_bio(nome= 'Ana Maria', especialização= 'Back-End', linguagem= 'Python')

# args *
def verifica_aluna(*args):
    if 'Aluna' in args and'Womakerscode' in args:
        return 'Ben-vinda aluna'
    return 'Eu não sei quem é você aluna'
print(verifica_aluna)
print(verifica_aluna(1, True, 'Womakerscode', 'Aluna'))
