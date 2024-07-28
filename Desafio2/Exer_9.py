# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

num_pares = 0
num_impares = 0

while True:
    num = int(input('Digite um número positivo (0 para encerrar): '))
    
    if num == 0:
        break

    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f'Quantidade de números pares: {num_pares}')

print(f'Quantidade de números ímpares: {num_impares}')

    
