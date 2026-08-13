#!/usr/bin/env python
# coding: utf-8

# ## Calculando o volume de um paralelepípedo

# In[1]:


print("Vamos calcular o volume de um paralelepípedo.")

base = float(input("Entre com a base: "))
largura = float(input("Entre com a largura: "))
altura = float(input("Entre com a altura: "))

volume = base * largura * altura

print(f"O volume é: {volume:.2f}")


# O fluxograma desse algoritmo seria representado dessa forma:
# 
# | Fluxograma |
# | :-- |
# | Elipse (inicio) |
# | Paralelograma (lendo variaveis) |
# | Retângulo (calculando volume) |
# | Retângulo de base omdulada (saída de dados) |
# | Elipse (fim do programa) |

# ## Operadores aritméticos:
# 
# São operadores que operam sobre duas variáveis (binários) e retornam um valor resultante da operação.
# 
# | Operador | Operação |
# | :-- | :-- |
# | + | Adição |
# | - | Subtração |
# | * | Multiplicação |
# | / | Divisão |
# | ** | Exponenciação |
# | // | Divisão de inteiros (chão) |
# | % | Resto da divisão de inteiros (módulo) |
# 
# Vamos exercitar esses operadores abaixo:

# In[2]:


x = 1.0
y  = 4.0
soma = x + y
print(f"soma: {soma}")
subtracao = y - x
print(f"subtração: {subtracao}")
multiplicacao = y * x
print(f"multiplicação: {multiplicacao}")
divisao = y / x
print(f"divisão: {divisao}")
exp = y * x
print(f"exponenciação: {exp}")
divisao_int = y // x
print(f"divisão de inteiros: {divisao_int}")
resto = y % x
print(f"resto inteiro: {resto}")


# Temos duas exceções no que se diz a operadores binários. Os operadores de soma e subtração podem operar em apenas uma variável.

# In[3]:


a = 10.0
b = -a
print(f"Usando o operador de subtração, inverto um número positivo: {b}")
b = +a
print(f"Usando o operador de adição, inverto um número negativo: {b}")


# O valor da variável **a** foi preservado, mas quando eu atribuo o valor de **a** para **b** posso inverter o sinal do valor, criando uma outra variável igual a **-a**.

# ### OPERADORES DE ATRIBUIÇÃO:
# Sâo operadores que operam sobre uma variável. Eles atribuem valores a variáveis, veja bem, basicamente eles pegam o valor armazenada na variável operanda, realizam uma operação aritmética com esse valor e o armazenam na mesma variável:
# |Operador|	Operação| 	Exemplo| 	Interpretação|
# |   :-- |   :-- |   :-- |   :---    |
# |   = 	|Atribuição simples| 	x = 2| 	x = 2|
# |   += 	|Soma e atribuição| 	x += 2| 	x = x + 2|
# |   -= 	|Subtração e atribuição| 	x -= 2| 	x = x - 2|
# |   *= 	|Multiplicação e atribuição| 	x *= 2| 	x = x * 2|
# |   /= 	|Divisão e atribuição| 	x /= 2| 	x = x / 2|
# |   **= |	Exponenciação e atribuição| 	x **= 2| 	x = x ** 2|
# |   //= |	Divisão inteira e atribuição| 	x //= 1|	x = x // 2|
# |   %= 	|Resto da divisão e atribuição| 	x %= 2| 	x = x % 2|
# 
# Vamos exercitar abaixo:

# In[4]:


numero = 4
print(numero) # Atribuição simples
numero += 2
print(numero) # atribuição com soma
numero -= 2
print(numero) # atribuição com subtração
numero *= 2
print(numero) # atribuição com multiplicação
numero /= 2
print(numero) # atribuição com divisão. Transforma em float
numero **= 2
print(numero) # atribuição com exponenciação
numero //= 4
print(numero) # atribuição com divisão. Mantém o tipo float, mas zera as casas decimais.
numero %= 2
print(numero) # atribuição do resto da divisão, mantém o tipo da variável


# ### OPERADORES LÓGICOS:
# Operadores booleanos testam condições lógicas e retornam um valor booleano True ou False:
# |Operador| 	Operação| 	Exemplo| 	Interpretação|
# |:--|:--|:--|:--|
# |and 	|E lógico| 	x and y| 	x e y|
# |or 	|OU lógico| 	x or y| 	x ou y|
# |not 	|NÃO lógico| 	not x| 	negue x|
# 
# **AND** - Testa se as variáveis a e b, se ambas forem verdadeiras = True, se não = False;
# 
# **OR** - Testa se uma das variáveis a ou b é verdadeira, se for = True, se não = False;
# 
# **NOT** - (Inversor) Retorna a negação da variável, se a = True, então False. Se a = False, então True.

# In[5]:


# Vejamos se você passou na matéria:
nota_azul = True
presenca = True

passou = nota_azul and presenca

print(passou)

# Vejamos se você paga meia-entrada:
id_estudante = True
carteira_pcd = False

meia_entrada = id_estudante or carteira_pcd

print(meia_entrada)

# Como está o tempo hoje:
chuva = False
posso_sair = not chuva
print(posso_sair)

# Vejamos se você é alfa
beta = False
alfa = not beta
print(alfa)


# ### OPERADORES DE COMPARAÇÃO (OPERADORES RELACIONAIS):
# Operadores que comparam variáveis de retornam True/False como resultado:
# |Operador| 	Operação| 	Exemplo| 	Interpretação|
# |:-- |:-- |:-- |:-- |
# |== 	|Comparação 	|x == y| 	x é igual a y?|
# |!= 	|Diferença 	|x != y| 	x é diferente de y?|
# |> 	|Maior que 	|x > y| 	x é maior que y?|
# |>= 	|Maior ou igual 	|x >= y| 	x é maior ou igual a y?|
# |< 	|Menor que 	|x < y| 	x é menor que y?|
# |<= 	|Menor ou igual| 	x <= y| 	x é menor ou igual a y?|

# In[6]:


x = 10
y = 20
comparar = (x == y)
print(comparar)
diferenciar = (x != y)
print(diferenciar)
maior = (x > y)
print(maior)
maior_igual = (x >= y)
print(maior_igual)
menor = (x < y)
print(menor)
menor_igual = (x <= y)
print(menor_igual)

