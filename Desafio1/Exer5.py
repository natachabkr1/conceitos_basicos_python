# 5. Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
# Renda até R$ 1.903,98: isento de imposto de renda;
# Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
# Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
# Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
# Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

salario_bruto = float(input("Informe seu salário bruto: "))

if salario_bruto <= 1903.98:
    desconto_imposto_renda = 0
    salario_liquido = salario_bruto - desconto_imposto_renda
    
elif salario_bruto > 1903.99 and salario_bruto <= 2826.65:
    desconto_imposto_renda = (salario_bruto * 7.5) / 100
    salario_liquido = salario_bruto - desconto_imposto_renda

elif salario_bruto > 2826.66 and salario_bruto <= 3751.05:
    desconto_imposto_renda = (salario_bruto * 15) / 100
    salario_liquido = salario_bruto - desconto_imposto_renda

elif salario_bruto > 3751.06 and salario_bruto <= 4664.68:
    desconto_imposto_renda = (salario_bruto * 22.5) / 100
    salario_liquido = salario_bruto - desconto_imposto_renda

elif salario_bruto > 4664.68:
    desconto_imposto_renda = (salario_bruto * 27.5) / 100   
    salario_liquido = salario_bruto - desconto_imposto_renda

print(f"Seu salário líquido é R$ {salario_liquido:.2f}")

    