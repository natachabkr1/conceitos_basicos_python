## 4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

quantidade_litros_combustivel = float(input("Qual a quantidade de litros de combustível consumido? "))
distancia_percorrida = float(input('Qual a distãncia percorrida? '))

consumo_medio_km = distancia_percorrida / quantidade_litros_combustivel
print(f'O consumo médio em km/l é: {consumo_medio_km:.2f}')