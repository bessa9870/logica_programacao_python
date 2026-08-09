# Introdução a lógica de programação em Python - Aula 1.2

## TÓPICO 1 - VARIÁVEIS E TIPOS DE DADOS

### 1.1 - A LINGUAGEM COMPUTACIONAL E AS VARIÁVEIS:
O computador só entende 0s e 1s (os códigos binários), umm endereço na memória pode ter dezenas de zeros e ums, por isso, usamos variáveis (fichas nomeadas) para acessar um endereço de memória afim de armazenar/modificar dados coletados num programa. É fundamental utilizar o tipo de memória correto para o dado coletado, um número, uma letra ou um texto, cada um tem seu tipo. Dessa forma, o programa fica mais leve e mais otimizado.

### 1.2 - UNIDADES DE ARMAZENAMENTO DE MEMÓRIA:
Bit (b): A menor unidade de armazenamento é o bite, que contêm apenas 0 ou 1;
Byte (B): Igual a 8 bits. Pode armazenar um caractere, como uma letra;
Kilobyte (KB): Igual a 1,024 bytes. Pode armazenar um pequeno arquivo de texto.
Megabyte (MB): Igual a 1,024 KB. Pode armazenar fotos ou arquivos de som pequenos.
Gigabyte (GB): Igual a 1,024 MB. Pode armazenar aplicativos, é bem usado em celulares.
Terabyte (TB): Igual a 1,024 GB. Pode armazenar arquivos massivos como um biblioteca de jogos.

### 1.3 - O QUE SÃO VARIÁVEIS:
A memória de um computador é como uma tabela gigante, cada célula tem seu endereço identificador, uma sequência grande de 0s e 1s. Por isso, usamos variáveis nomeadas. Num programa em Python onde é necessário atribuir um número de identificação ao usuário, basta nomear uma variável e atribuir o valor:
    
| Variável | Exemplo de Código |
| :--- | :--- |
| ID do Usuário | `id_usuario = 15` |

### 1.4 - A TIPAGEM EM PYTHON:
O próprio Python vai inserir o 15 na memória, alocando o espaço perfeito (nem um byte a mais ou a menos). Sempre que você quiser recuperar esse valor, basta chamar o identificador "id_usuario", muito mais simples do que digitar dezenas de 0s e 1s.

### 1.5 - TIPOS DE DADOS
O Python separa seus dados em tipos, chanmamos tipos de dados, definindo os valores representados e possível operações, por exemplo: somar dois números inteiros (int + int) é possível, mas somar uma booleana com uma int(bool + int) não. Vejamos os tipos primitivos:

#### Tipos primitivos
| Tipo de dado | Tipo | Valor possível |
| :-- | :-- | :-- |
| Lógico | bool | True/False |
| Números inteiros | int | Um número inteiro qualquer (1, 2, 10..)|
| Números decimais (ponto flutuante) | float | Um número com casas decimais (1.1, 10,155...)|
| Texto (string) | str | sequência de caracteres (qualquer caractere abc123!@#...) |
Varíaveis primitivas simples só aceitam 1 valor por variável

Além dos tipos simples, o Python possui tipos compostos, variáveis que aceitam mais de um valor por vez, como textos e listas: 

#### Tipos compostos
| Tipo de dado | Tipo | Possíveis valores |
| :-- | :-- | :-- |
| Lista de elementos por índice | list | elementos enumerados (nomes, números...) |

---------------------------------------------------------------------------

## TÓPICO 2 - ENTRADA, SAÍDA E CONCATENAÇÃO DE STRINGS

### 2.1 - FERRAMENTAS DE ENTRADA E SAÍDA
Num programa orientado ao mundo real, é necessário haver interatividade com o usuário. Os dados a serem computados devem vir do usuário (na maioria das vezes), é aí que entram as estruturas de entrada via teclado e saída de dados via monitor.

#### Ferramentas de entrada e saída
| Função | O quê faz? |
| :-- | :-- |
| input() | parâmetro usado para ler um valor e atribuir a variável À esquerda |
| print() | uma função que vai ler e exibir o que estiver dentro dos parênteses |

### 2.2 - ENTRRDA, CONVERSÃO DE DADOS:
Quando se usa input para coletar dados, ele sempre retorna string. É necessário realizar uma conversão para o tipo de dado que o programador espera receber.
| Tipo desejado | Sintaxe |
| :-- | :-- |
| int | variavel = int(input("Entre com um inteiro: ")) |
| float | variavel = float(input("Entre com um decimal: ")) |

*Obs: Em Python não existe diferença de char e array de char como em C. Para o Python todo char é um array de char, mesmo com tamanho 1.*


### 2.3 - SAÍDAS FORMATADAS COM PRINT:
Existem três formas de realizar uma saída de dados com a função print:

*(Vamos usar duas variáveis para ilustração)*
    
| nome = João | idade = 20 |
| :-- | :-- |

| f.string (Mais moderna) | print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.") |
| :-- | :-- |

Basta colocar a letra f antes das aspas e o nome da variável direto dentro de chaves { }:

| Separar por vírgula | print("Olá, meu nome é", nome, "e eu tenho", idade, "anos.") |
| :-- | :-- |

A própria função print() do Python aceita múltiplos valores separados por vírgula. Ela junta tudo e coloca um espaço automaticamente entre eles:

| Estilo C | print("Olá, meu nome é %s e eu tenho %d anos." % (nome, idade)) |
| :-- | :-- |

### 2.4 - OPERAÇÃO DE CONCATENAÇÃO DE STRINGS
Para concatenar uma string, basta usar o operador de soma +.
nome = 'João'
sobrenome = "Bessa"
nome_completo = nome + ' ' + sobrenome

O ' ' é uma string de tamanho 1 com espaço para que os valores não fiquem grudados.











