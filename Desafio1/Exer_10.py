## 10. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade

nome = input('Qual o seu nome: ')
lugar = input('De qual Cidade / Estado você está falando? ')
profissao = input('Qual a sua profissão? ')
objetivo = input('Qual o seu objetivo com este curso? ')

print(f'Olá {nome}! Temos participantes de várias regiões do Brasil e é um prazer ter você de {lugar} também!')
print(f'Areditamos que juntas podemos alcançar nossos objetivos, e quem sabe você também conseguirá alcançar o objetivo de {objetivo} que está em busca.')
print('Até breve!')
