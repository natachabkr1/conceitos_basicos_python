## 1. Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

soma = numero1 + numero2
print(f'A soma dos números digitados é {soma}')

subtracao = numero1 - numero2
print(f'A subtração dos números digitados é {subtracao}')

multiplicacao = numero1 * numero2
print(f'A multiplicação dos números digitados é {multiplicacao}')

divisao = numero1 / numero2
print(f'A divisão dos números digitados é {divisao:.2f}')
