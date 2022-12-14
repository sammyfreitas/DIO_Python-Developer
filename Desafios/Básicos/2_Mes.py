''' 
Desafios Básicos Formação Python Developer
2 / 3 - Mês
 Básico
 Princípios Básicos

Desafio
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

Exemplo de Entrada	
4 

Exemplo de Saída
April

''' 

'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
- "dict{}": dicionários possuem uma relação de chave - valor. Para cada chave haverá um valor.
'''
month = int(input())
month_dict = {1: 'January' , 2: 'February' , 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December' }
if month in range (1, 13):
  print(month_dict[month])  
''' 
  TODO Faça uma relação entre as possíveis entradas e os meses (em inglês).
  TODO Imprima o valor de cada chave em relação as entradas do programa.
'''
'''
T = input()
test_tweet = len(T)
if test_tweet <= 140:
    print ('TWEET')
elif test_tweet > 140:
    print('MUTE')
else:
    print('Digite seu Tweet')