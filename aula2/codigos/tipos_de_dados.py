#!/usr/bin/env python
# coding: utf-8

# # Tipos de dados em Python 

# ## Tipos primitivos:
# | Tipo de dado | Tipo | Valor possível |
# | :-- | :-- | :-- |
# | Lógico | bool | True/False |
# | Números inteiros | int | Um número inteiro qualquer (1, 2, 10..)|
# | Números decimais (ponto flutuante) | float | Um número com casas decimais (1.1, 10,155...)|
# | Texto (string) | str | sequência de caracteres (qualquer caractere abc123!@#...) |
# 
# *(São variáveis simples, cada variável aceita apenas um valor por vez)*

# In[1]:


peso_usuario = 66.5
altura_usuario = 1.74
aprendendo_python = True
idade_usuario = 20
nome_usuario = "João Bessa"


# O Python não é rigoroso com a tipagem de variáveis. O próprio através da atribuição do valor, 
# deduz o tipo da variável. Por exemplo: quando eu atribuí 66.4, mesmo sem declarar o tipo da
# variável, o Pytthon já sabe o tipo correto para ponto flutuante.

# In[2]:


peso_usuario


# In[3]:


type(peso_usuario)


# In[4]:


type(nome_usuario)


# ## Tipos compostos:
# | Tipo de dado | Tipo | Possíveis valores |
# | :-- | :-- | :-- |
# | Lista de elementos por índice | list | elementos enumerados (nomes, números...) |
# | lista de conjuntos por índice | set | elementos enumerados, vai ignorar repetições (nomes, números...) |
# 
# *(São variáveis em linha que aceitam mais de um valor por vez, como num vetor em C)*

# In[5]:


minha_lista1 =  {1, 2, 3, 4}
type(minha_lista1)


# In[6]:


minha_lista2 = [1, 2, 3, 4]
type(minha_lista2)


# In[7]:


meus_dados = ["João Bessa", 20, True]
type(meus_dados)


# Como dito antes, é possível acessar um dado usando seu índice

# In[8]:


meus_dados [1]


# In[9]:


meus_dados[-1]

