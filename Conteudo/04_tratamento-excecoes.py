# Tratamento de ERROS

def divisao(a,b):
    try:   #tente...
        resultado = a/b
        print(resultado)

    except ZeroDivisionError:   # qual a exceção aquele caso
        print('Erro: Impossível dividir por zero')
    except TypeError as e:   # e - nos permite trazer mais detalhes do erro
        print(f'Erro: O tipo do dado informado não está correto. \n Detalhes: {e}')

    else:
        print('Sem exceções')

# \n - quebra a informação para a próxima linha

# divisao(10,2)
# divisao(10,0)

divisao(10, 'Womakerscode')

