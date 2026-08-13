# Introdução À lógica de programação em Pytthon - Aula 1.3

## TÓPICO 1 - OPERAÇÕES COM VARIÁVEIS:
Programas complexos fazem operações, sejam elas adicão, subtração, multiplicação... Operações sempre estaram presentes em uma grande parcela dos programas que você irá desenvolver no futuro. Os operadores aritméticos das quatro operações não são diferentes do que aprendemos na escola.

Vamos pegar um algoritmo que calcula o volume de um paralelepípedo:
```Python
print("Vamos calcular o volume de um paralelepípedo.")

base = float(input("Entre com a base: "))
largura = float(input("Entre com a largura: "))
altura = float(input("Entre com a altura: "))

volume = base * largura * altura

print(f"O volume é: {volume:.2f}")
```
---
## TÓPICO 2 - OPERADORES E PRECEDÊNCIA DE VALORES:
É claro que em Python não existem apenas operadores aritméticos, existem dezenas deles, podemos classificá-los por grupos:
| Grupo | Finalidade |
| :-- | :-- |
| Aritméticos | Nos ajudam a fazer cálculos matemáticos |
| Atribuição | Nos ajudam a armazenar dados e facilmente modificar variáveis em memória; |
| Lógicos | Como o próprio nome já anuncia, possibilitam a construção de expressões lógicas |
| Comparação ou relacionais | Nos ajudam a comparar valores e expressões |
| Lógicos bit-a-bit | Avaliam cada um dos bits das variáveis que os utilizam |
| Identidade e de pertencimento | Nos ajudam a comparar variáveis e a saber se elas estão no mesmo local da memória do computador |

### OPERADORES ARITMÉTICOS: 
São operadores que operam sobre duas variáveis (operadores binários) e retornam um valor resultante da operação entre ambas:
| Operador | Operação |
| :-- | :-- |
| + | Adição |
| - | Subtração |
| * | Multiplicação |
| / | Divisão |
| ** | Exponenciação |
| // | Divisão de inteiros (chão) |
| % | Resto da divisão de inteiros (módulo) |

### OPERADORES DE ATRIBUIÇÃO:
Sâo operadores que operam sobre uma variável (operadores unários). Eles atribuem valores a variáveis, veja bem, basicamente eles pegam o valor armazenada na variável operanda, realizam uma operação aritmética com esse valor e o armazenam na mesma variável:
|Operador|	Operação| 	Exemplo| 	Interpretação|
|   :-- |   :-- |   :-- |   :---    |
|   = 	|Atribuição simples| 	x = 2| 	x = 2|
|   += 	|Soma e atribuição| 	x += 2| 	x = x + 2|
|   -= 	|Subtração e atribuição| 	x -= 2| 	x = x - 2|
|   *= 	|Multiplicação e atribuição| 	x *= 2| 	x = x * 2|
|   /= 	|Divisão e atribuição| 	x /= 2| 	x = x / 2|
|   **= |	Exponenciação e atribuição| 	x **= 2| 	x = x ** 2|
|   //= |	Divisão inteira e atribuição| 	x //= 1|	x = x // 2|
|   %= 	|Resto da divisão e atribuição| 	x %= 2| 	x = x % 2|

### OPERADORES LÓGICOS:
Operadores booleanos testam condições lógicas e retornam um valor booleano True ou False:
|Operador| 	Operação| 	Exemplo| 	Interpretação|
|:--|:--|:--|:--|
|and 	|E lógico| 	x and y| 	x e y|
|or 	|OU lógico| 	x or y| 	x ou y|
|not 	|NÃO lógico| 	not x| 	negue x|

### OPERADORES DE COMPARAÇÃO (OPERADORES RELACIONAIS):
Operadores que comparam variáveis de retornam True/False como resultado:
|Operador| 	Operação| 	Exemplo| 	Interpretação|
|:-- |:-- |:-- |:-- |
|== 	Igualdade 	|x == y| 	|x é igual a y?|
|!= 	Diferença 	|x != y| 	x é diferente de y?|
|> 	|Maior que 	|x > y| 	x é maior que y?|
|>= 	|Maior ou igual| 	x >= y| 	x é maior ou igual a y?|
|< 	|Menor que| 	x < y| 	x é menor que y?|
|<= 	|Menor ou igual| 	x <= y| 	x é menor ou igual a y?|

### OPERADORES DE IDENTIDADE:
Testam se variáveis com nomes diferentes se referem ao mesmo local na memória:
|Operador| 	Exemplo| 	Interpretação|
| :-- | :-- | :-- |
|is| 	x is y| 	x e y estão endereçando o mesmo local de memória? |
|is not| 	x is not y| 	x e y não estão endereçando o mesmo local de memória? |

### OPERADORES DE IDENTIDADE:
Testa se uma variável está dentro da segunda:
|Operador| 	Exemplo| 	Interpretação|
|:-- |;-- |:-- |
|in| 	x in y| 	x faz parte de y? x está em y?|
|not in| 	x not in y| 	x não faz parte de y? x não está em y?|

---
## TÓPICO 3 - PRECEDÊNCIA DE OPERADORES:
Com operadores podemos realizar operações mais complexas, mas é necessário ter o conhecimento sobre a precedência desses operadores. Precedência de valores é uma convenção utilizada para evitar erros em operações complexas, onde  quanto maior a precedência de um operador, maior a prioridade dele dentro da operação. Vamos descobrir qual é a convenção adotada pelo Python para isso.

*Se em uma operação existem dois operadores de mesmo nível de precedência, será resolvido o operador mais à esquerda.*

|Precedência (maior a menor)|
|:--    |:--    |:--   |
|Precedência| 	Operadores| 	Nomes|
|1|	** 	|Exponenciação|
|2| 	+x , -x , ~x| 	Positivo, Negativo, negação bit-a-bit|
|3| 	*, /, //, %| 	Multiplicação, divisão, divisão inteira e resto da divisão|
|4| 	+, -| 	Adição, subtração|
|5| 	<<, >>| 	Deslocamento bit-a-bit|
|6| 	&| 	E lógico bit-a-bit|
|7| 	^| 	OU exclusivo lógico bit-a-bit|
|8|     | | 	Ou lógico bit-a-bit|
|9| 	<, <=, >, >=, !=, ==| 	Operadores de comparação|
|10| 	not x| 	Negação lógica|
|11| 	and| 	E lógico|
|12| 	or| 	OU lógico|

*Usar parênteses quebra a precedência, o que estiver dentro deles será calculado primeiro, mas, tenha em mente que dentro dos parênteses também haverá precedência de valores*
| Exemplos: |
| :-- |
|  x = 1 + 2 * 3 * 5 = 31; |
|  x = (1 + 2 * 3) * 5 = 35; |
|  x = (1 + 2) *( 3 * 4) = 36 |
*Entre dois parênteses será executado primeiro o mais à esquerda.*
