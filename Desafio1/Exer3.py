## 3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.


km = int(input('Digite a quantidade de quilometros(km): '))

# Convertendo de quilômetros para metros
m = km * 1000

# Convertendo de metros para centímetros
cm = m * 100

# Convertendo de centímetros para milímetros

mm = cm * 10

print(f'Os {km} km equivalem a {m} m, {cm} cm e {mm} mm.')

