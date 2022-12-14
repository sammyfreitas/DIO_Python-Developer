''' 
Desafios Básicos Formação Python Developer
1 / 3 - Tuitando
 Básico
 Princípios Básicos

DESAFIO
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".


Exemplo de Entrada	
RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap

Exemplo de Saída
TWEET


IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''

''' 
TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
'''
T = input()
test_tweet = len(T)
if test_tweet <= 140:
    print ('TWEET')
elif test_tweet > 140:
    print('MUTE')
else:
    print('Digite seu Tweet')