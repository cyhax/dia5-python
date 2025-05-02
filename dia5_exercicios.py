# DIA 5 - Exercícios finais do Mundo 1 (Curso em Vídeo)

# Exercício 28 - Jogo de Adivinhação
import random
res = int(input('Digite um número de 0 a 5: '))
sort = random.randint(0, 5)
print('Você acertou!' if sort == res else f'Você errou! O número era {sort}.')

# Exercício 29 - Radar eletrônico
vel = int(input('Digite sua velocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado!')
    print(f'A multa ficou em R${multa:.2f}')
else:
    print('Você não foi multado.')

# Exercício 30 - Par ou Ímpar
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')

# Exercício 31 - Preço da Passagem
km = float(input('Quantos km tem a viagem? '))
if km < 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'A passagem vai ficar R$ {preco:.2f}')

# Exercício 32 - Ano Bissexto (sem usar and/or)
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano de {ano} é bissexto.')
        else:
            print(f'O ano de {ano} não é bissexto.')
    else:
        print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')

# Exercício 33 - Maior e menor número
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

# Exercício 34 - Aumento de Salário
salario = float(input('Qual o seu salário? '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print(f'Seu novo salário com aumento é R$ {novo_salario:.2f}')

# Exercício 35 - Verificador de Triângulo (sem usar and)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2 + s3:
    if s2 < s1 + s3:
        if s3 < s1 + s2:
            print('Os segmentos PODEM formar um triângulo!')
        else:
            print('Os segmentos NÃO podem formar um triângulo.')
    else:
        print('Os segmentos NÃO podem formar um triângulo.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
