#Snake desistiu de comer ovos de pássaros já que ela descobriu da pior maneira que eles ficam muito bravos, e andou buscando novas opções. Em sua busca, Snake encontrou ovos de camaleão, que possuem uma incrı́vel curiosidade: aqueles que comem os ovos mudam de cor. Fascinada por essa descoberta, Snake começou a coletar inúmeros ovos dos camaleões, que fizeram armadilhas para Snake. Em alguns ninhos foram colocados ovos envenenados, que ao serem tocados, eles explodem e provocam sono instantaneamente. Assim, ao encontrar um ovo envenenado, Snake dorme por alguns segundos e os camaleões conseguem recuperar dois ovos. Ela quis saber então, ao fim de três caçadas, com quantos ovos ela ficou e te pediu ajuda, já que você é um excelente programador. Assim, dadas as quantidades de ovos coletados e o número de ovos envenenados em cada caçada diga quantos sobraram.
#Entrada: A entrada é composta na primeira linha por 3 inteiros, ‘Q1’, ‘Q2’ e ‘Q3’ (6 <= ‘Q1’,‘Q2’,‘Q3’ <= 20), representando a quantidade de ovos coletados em cada uma das caçadas. Na segunda linha serão dados 3 inteiros, ‘E1’, ‘E2’ e ‘E3’ (0 <= ‘E1’,‘E2’,‘E3’ <= 2), representando a quantidade de ovos envenenados em cada uma das caçadas.
#Saída: Na saída será apresentada a quantidade de ovos que sobraram das caçadas.

from functools import total_ordering


Q1, Q2, Q3 = input().split()
E1, E2, E3 = input().split()

Q1 = int(Q1)
Q2 = int(Q2)
Q3 = int(Q3)
E1 = int(E1)
E2 = int(E2)
E3 = int(E3)

cacada1 = int(Q1 - E1) - int(E1 * 2)
cacada2 = int(Q2 - E2) - int(E2 * 2) 
cacada3 = int(Q3 - E3) - int(E3 * 2)

totalOvos = cacada1 + cacada2 + cacada3

print(totalOvos)