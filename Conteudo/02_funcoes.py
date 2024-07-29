# Funções - organizam os códigos - grupos de instruções que executam uma tarefa

'''def soma():  # definição da função soma
    calculo = 10+2
    print(f'O resultado da soma é: {calculo}')

def subtracao():   
    sub = 10-2  # a variável não pode ter o memso nome da função
    print(f'O resultado da subtração é: {sub}')
    multiplicacao()  # chamada função dentro de uma outra função

def multiplicacao():   
    mult = 10*2  
    print(f'O resultado da multiplicação é: {mult}')

soma()  # chamada da função soma
subtracao()''' 

# Usuário digitando os números - PARÂMETROS

def soma(num1, num2):  # definição da função soma
    
    calculo = num1 + num2
    print(f'O resultado da soma é: {calculo}')

def subtracao(num1,num2): 
      
    sub = num1 - num2  # a variável não pode ter o memso nome da função
    print(f'O resultado da subtração é: {sub}')
      
def multiplicacao(num1, num2):   
    mult = num1 * num2  
    print(f'O resultado da multiplicação é: {mult}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2)  # chamada da função soma
subtracao(num1, num2) 
multiplicacao(num1, num2)
