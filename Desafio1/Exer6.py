# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# avião = 600 km/h
# carro = 100 km/h
# ônibus = 80 km/h



distancia_viagem = float(input("Qual a distância percorrida na viagem? "))


# Calculando o tempo de viagem  

tempo_aviao = distancia_viagem / 600
tempo_carro = distancia_viagem / 100
tempo_onibus = distancia_viagem / 80

print(f"O avião leva {tempo_aviao:.2f} horas para chegar ao destino.")
print(f"O carro leva {tempo_carro:.2f} horas para chegar ao destino.")
print(f"O ônibus leva {tempo_onibus:.2f} horas para chegar ao destino.")
