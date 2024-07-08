# %%
# Isto é um comentário
# Isto é outro comentário
print("Olá mundo") # Isto é um comentário
# %%
'''
Este é um comentário
ou comentário continua aqui
aqui ainda continua
e aqui termina
'''
# %%
print("Olá mundo")
print(10)
print(20.5)
# %%
print("Maça", 20 , 30.45)

# %%
print("Maçã", "Pera", "Uva", sep="-")
# %%
print("Maçã ", " Pera", end = " Fim", sep=' ')
# %%
print("Este é um texto longo, \n eu quero quebrar a linha")
# %%
print("Maçã", "Pera",  sep='\n')

# %%
# Tradicional, parecido com a Linguagem C
print("A pontuação total de %s foi %s pontos" % ("Fernando", "10"))

# %%
# Utilização do .format (Desuso)
print("A pontuação total de {} foi {} pontos".format("Fernando", "10"))

# %%
#Concatenação de Strings
print("A pontuação total de" + " Fernando" + " foi" + " 10 " + "pontos")
# %%
#Fstring
print(f"A pontuação total de {"Fernando"} foi {10} pontos")

# %%
# Atividade

''' 1- Realize o print do seu nome completo, sua idade e sua altura utilizando um print para cada valor '''
print(f"Gustavo")
print(f"38")
print(f"1.73")


# %%
''' 2- Realize o print do seu nome completo, sua idade e sua altura utilizando apenas um print para todos os
valores '''
print(f"{"Gustavo"} {38} {1.73} ")

# %%
'''
3 - Realize o print de 3 números de sua escolha em um mesmo print, mas separados pelo caractere '-'
'''
print(45, 143.14, 7894, sep="-")

# %%
# Variaveis
# Variaveis tem começar com letra ou sobreescrito (underline) _. Somente pode conter letras, numero e _. Letras mauisculas e minusculas são tratadas diferentes.
# Ex: Nome NOME nome
# %%
_numero = 1
Numero = 2
numero = 3
numero123 = 4
print(_numero, Numero, numero,numero123)
# %%
numero = 10
print(numero)
numero = 20
print(numero)

# %%
texto = "Olá mundo!"
print(texto)
# %%
# Tipos Primitivos
variavel = None
print(variavel)

# %%
inteiro = 10
print(inteiro)
# %%
decimal = 1.53
print(decimal)
# %%
texto = "olá, isto é um texto"
print(texto)
# %%
var = True
print(var)
var = False
print(var)
# %%
var1 = 10
var2 = var1
print(var2)
# %%
var = None
print(var)
var = 1
print(var)
var = "Texto"
print(var)
# %%
saldoBancario = 100 # Pascal Case
SaldoBancario = 100 # Camel Case
saldo_bancario = 100 # snake case
# %%
# 1. Crie uma variável de cada tipo e ponha algum valor escolhido. Em seguida, printe todos esses valores

primeiravar = "Texto"
segundavar = 45
terceiravar = 456.48
quartavar = True

print(f"{primeiravar}, {segundavar}, {terceiravar}, {quartavar} ")

# %%
# 2. Crie variáveis para guardar seu nome, CPF e uma que indique se você está casado, em seguida printe
# esses valores separadamente, mas não esqueça de printar junto o que eles significam

nome = "Gustavo"
cpf = "123.456.789-00"
casado = True
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Casado: {casado}")

# %%
# Formatacao
# %s - texto
# %d - inteiro
# %f - ponto flutuante (real)
# %%
nome = "Ana"
texto_formatado = "O nome dela é %s " % (nome)
print(texto_formatado)
# %%
nome = "Rodrigo"
idade = 23
altura = 1.73
texto = "Meu nome é %s. Tenho %d anos e tenho %f metros de altura" % (nome, idade, altura)
print(texto)
# %%
numero_gigante = 1.123456789
print("Número gigante formatdo: %.0f" % (numero_gigante))
# %%
valor = False
print("O valor é %s" % (valor))
print("O valor é %d" % (valor))
# %%
decimal = 23.4566
print("A parte inteira é %d" % (decimal))
# %%
texto = "Olá, assim se quebra uma linha, \n\t entendeu como quebra a linha? \n\t\t fim"
print(texto)
# %%
texto = "Deixa a \'palavra\' entre aspas"
#texto = "Deixa a 'palavra' entre aspas"
print(texto)
# %%
# 1 - Escreva e formate a data em que você nasceu no formato dia/mês/ano. Não esqueça de criar 3 variaveis
# para guardar o dia, mês e ano.
# Exemplo de saída:
# Eu nasci em 30/09/1998

dia_nasc = 29
mes_nasc = 2
ano_nasc = 1990
data_nascimento = f"{dia_nasc}/{mes_nasc}/{ano_nasc}"
print(f"Eu nasci em {data_nascimento}")

# %%
# 2 - Escreva e formate a hora e minuto atual. Não esqueça de criar duas variáveis para guardar a hora e
# e minuto
# Exemplo de saída:
# Agora são 22 horas e 37 minutos

from datetime import datetime

data_e_hora_atuais = datetime.now()
hora = data_e_hora_atuais.strftime('%H')
minuto = data_e_hora_atuais.strftime('%M')
saida = f"Agora são {hora} horas e {minuto} minutos"
print(saida)

# %%
# 3 - Escreva um programa que contém um número PI, que deve ter o valor exato de 3.14159265359. Agora formate
# esse valor para ter apenas cinco casas decimais.

# Exemplo de saída:
# O PI é 3.14159
# Import math Library

import math
num_pi = math.pi
print(num_pi)

print("O PI é %.5f" % num_pi)
# %%
# Operadores Aritmeticos
# %%
print(10 + 20)
# %%
numero = 10 + 10.5
print(numero)
# %%
outro_numero = 30 + numero
print(outro_numero)
# %%
numero = 20 - 10
print(numero)
# %%
numero = 20*2
print(numero)
# %%
numero = 10 / 3
print(numero)
# %%
numero = 10 // 3 # Trazer apenas a parte inteira
print(numero)
# %%
numero = 2 ** 4
print (numero)
# %%
numero = 4 % 3 # Resto
print(numero)
# %%
# Ordem de Prioridade - Operadores
'''
1. ** (exponeciação)
2. * (multiplicação)
3. / (divisão)
4. % (resto da divisão ou mod)
5. // (Divisão inteira)

Para resolver as priorizações, basta usar o parenteses no calculo
'''
# %%
nume1 = 10 * 2 + 1
print(nume1)
# %%
nume1 = 10 * (2 + 1)
print(nume1)

# %%
nume1 = 3 * 3-9
print(nume1)

# %%
nume1 = 3 * (3-9)
print(nume1)

# %%
nume1 = 20
nume2 = 40
nume3 = 60
resultado = nume1 + nume2 + nume3
print(resultado) 
# %%
resultado = resultado * 2
print(resultado)
# %%
a = 1
a += 1 # a = a + 1
print(a)

# %%
'''
1 - Crie um programa que possui duas variáveis, uma recebe o ano em que estamos e a outra o ano em que nasceu.
Em seguida, subtraia ambas para receber uma estimativa de quantos anos você tem. Mostre esse valor na saída do
programa
'''
ano_atual = 2024
ano_nasc = 1986
idade = ano_atual - ano_nasc
print(f"A sua idade é de {idade} anos")

# %%
'''
2. Crie um programa que faz a média arimitética entre três números. Estes números devem ser 
salvos em uma variável. Mostre esse valor na saída do programa.
'''
n1 = 45
n2 = 54
n3 = 85
media = (n1 + n2 + n3) / 3
print(f"A Média dos números é {media}")
# %%
'''
3. Crie um programa que calcule o IMC (Indice de Massa Corporal). O IMC é dado pelo peso em KG dividido
pela altura em metros elevado ao quadrado. Salvar esses valores em uma variável. Mostre o valor na saida
do programa.
'''
peso = 126
altura = 1.73
imc = peso / (altura ** 2)

print (f"Para você quem pesa {peso}Kg e tem {altura}m, o seu IMC é {imc}.")

# %%
'''
4 - (Desafio) - Você tem um determinado números de ovos de Páscoa para dividir entre um determinado 
números de pessoas (duas variáveis iniciais). Determine quantos ovos ficarão por pessoa e quantos ovos 
sobrarão, pois não puderam ser dividos igualmente. Lembre o número de ovos por pessoa é um número inteiro.
'''
ovos = 47
pessoas = 3
ovos_pessoa = ovos // pessoas
ovos_sobra = ovos % pessoas
print(f"Ficarão {ovos_pessoa} para cada um. E sobraram {ovos_sobra} ovos")

# %%
