# Lucas está jogando x1 contra seu amigo Pedro no counter strike, porém ele está com dificuldade em saber quem obteve a maior pontuação geral de abates.
# Considerando que eles jogaram 3 partidas, sua tarefa é elaborar um programa que dada a pontuação de Pedro e Lucas em cada uma das 3 partidas diga quem obteve o maior número de abates total.
# Entrada: A entrada consiste em 3 linhas contendo 2 inteiros ‘L’, ‘P’ (1 <= ‘L’, ‘P’ <= 100) em cada uma, sendo que L indica a pontuação de Lucas e P a pontuação de Pedro.
# Saída: A saída consiste em uma linha contendo a palavra “Empate”, caso os dois empatem, o nome “Pedro” caso Pedro tenha obtido uma pontuação de abates total maior que a de Lucas, ou o nome “Lucas”, caso Lucas tenha abates total maior que Pedro.

L1, P1 = input().split()
L2, P2 = input().split()
L3, P3 = input().split()

L1 = int(L1)
P1 = int(P1)
L2 = int(L2)
P2 = int(P2)
L3 = int(L3)
P3 = int(P3)

TL = L1 + L2 + L3
TP = P1 + P2 + P3

if TL > TP:
    print("Lucas")
elif TL == TP:
    print("Empate")
else:
    print("Pedro")