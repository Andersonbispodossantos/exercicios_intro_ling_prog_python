# O Lobo Mau resolveu parar um pouco com as maldades, decidiu abrir uma empresa de entregas e convidou Chapeuzinho Vermelho para ser sua sócia.
# Certo dia, Chapeuzinho precisou levar doces e bolos para sua vovozinha. Como todos sabem, ela mora longe, o caminho é deserto e o Coelho Mau mora ali por perto. Sim, como o Lobo virou empresário, alguém tinha que tomar seu lugar na floresta. Assim, Chapeuzinho pediu uma carona ao seu sócio e lá foi ela pela estrada a fora, já não tão sozinha, levar os bolos e doces para a vovozinha.
# Ao chegar na casa da vovozinha eles foram saborear as deliciosas guloseimas. Como o Lobo Mau é muito guloso, Chapeuzinho resolveu distribuir ‘N’ doces um de cada vez para cada um deles. Assim, ela comia um, dava um para a vovozinha e um para o lobo, depois comia mais um, dava outro para a vovozinha e outro para o lobo, e assim por diante.
# Eles querem saber então, após ‘N’ doces, quantos doces cada um comeu. 
# Entrada: A entrada é composta por um inteiro ‘N’ (1 <= ‘N’ <= 100), representando a quantidade total de doces comidos pela Chapeuzinho, pela vovozinha e pelo Lobo Mau.
# Saída: Na saída será apresentada a quantidade de doces que cada um comeu. Imprima um nome por linha, seguindo a ordem: Chapeuzinho Vermelho, Vovozinha, Lobo Mau.

N = int(input())

quociente = int(N / 3)
resto = int(N % 3)

if resto == 0:
    print("Chapeuzinho Vermelho " + str(quociente))
    print("Vovozinha " + str(quociente))
    print("Lobo Mau " + str(quociente))
elif resto == 1:
    print("Chapeuzinho Vermelho " + str(quociente + 1))
    print("Vovozinha " + str(quociente))
    print("Lobo Mau " + str(quociente))
else:
    print("Chapeuzinho Vermelho " + str(quociente + 1))
    print("Vovozinha " + str(quociente + 1))
    print("Lobo Mau " + str(quociente))


