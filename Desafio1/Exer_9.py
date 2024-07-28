## 9. Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício

exercicio_fisio_semana= float(input('Quantas horas por semana você pratica exerício? '))
exercicio_em_minutos = exercicio_fisio_semana * 60
calorias_queimadas_minuto_semana = exercicio_em_minutos * 5
calorias_queimadas_mes = calorias_queimadas_minuto_semana * 4

print(f'Você queimou {calorias_queimadas_mes:.1f} calorias no mês!')
