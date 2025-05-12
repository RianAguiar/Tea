# pede para o usuario digite o tipo do cha
cha = int(input())
'''a linha de comando abaixo pede para o usuario dar as possiveis respostas de cha
   em seguida vai dividir o input em uma lista de varias strings''' 
respostas = input().split()
''' a linha de comando abaixo irá pegar as strings e 
    transformará todas elas em valor int numa lista ordenada, 
    por conta do comando list(map(int, 'lista de strings'))'''
respostas = list(map(int,respostas))
'''a linha de comando abaixo irá contar quantos valores da 'respostas' coincidem com
    o valor da variavel 'cha' '''
contagem_de_respostas = respostas.count(cha)
print(contagem_de_respostas)
