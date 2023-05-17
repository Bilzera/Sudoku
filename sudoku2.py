matriz = [[0, 0, 6, 0, 0, 0, 0, 5, 0], 
          [2, 0, 1, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 7, 0, 0, 0, 1, 4], 
          [0, 0, 0, 0, 0, 0, 4, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 9, 0, 0, 0, 0, 0, 0], 
          [5, 7, 0, 0, 0, 2, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 2, 0, 9], 
          [0, 1, 0, 0, 0, 0, 3, 0, 0]]


matrizQuadradinho = [[0.0, 0.1, 0.2, 1.0, 1.1, 1.2, 2.0, 2.1, 2.2], 
                     [0.3, 0.4, 0.5, 1.3, 1.4, 1.5, 2.3, 2.4, 2.5], 
                     [0.6, 0.7, 0.8, 1.6, 1.7, 1.8, 2.6, 2.7, 2.8], 
                     [3.0, 3.1, 3.2, 4.0, 4.1, 4.2, 5.0, 5.1, 5.2], 
                     [3.3, 3.4, 3.5, 4.3, 4.4, 4.5, 5.3, 5.4, 5.5], 
                     [3.6, 3.7, 3.8, 4.6, 4.7, 4.8, 5.6, 5.7, 5.8], 
                     [6.0, 6.1, 6.2, 7.0, 7.1, 7.2, 8.0, 8.1, 8.2], 
                     [6.3, 6.4, 6.5, 7.3, 7.4, 7.5, 8.3, 8.4, 8.5], 
                     [6.6, 6.7, 6.8, 7.6, 7.7, 7.8, 8.6, 8.7, 8.8]]


possibilidades = {}

for linha in range (0, 9):
        for coluna in range (0, 9):

                '''Verifica se é realmente necessário passar nesse FOR cheio de IF'''
                if matriz[linha][coluna] == 0:

                        matrizComparacao = []
                        for numbers in range (0, 9):

                                '''Adiciona o que está na linha'''
                                if numbers + 1 in matriz[linha]:
                                        matrizComparacao.append(numbers + 1)

                                '''Adiciona o que está na coluna'''
                                if matriz[numbers][coluna] != 0:
                                        matrizComparacao.append(matriz[numbers][coluna])

                                '''Adiciona o que está na diagonal 1'''
                                if matriz[numbers][numbers] != 0 and linha == coluna:
                                        matrizComparacao.append(matriz[numbers][numbers])

                                '''Adiciona o que está na diagonal 2'''
                                if matriz[numbers][8 - numbers] != 0 and linha + coluna == 8:
                                        matrizComparacao.append(matriz[numbers][8 - numbers])

                                '''Adiciona o que está no quadradinho de 9'''
                                if linha + coluna/10 in matrizQuadradinho[numbers]:
                                        for posQuad in range (0,9):
                                                x = matrizQuadradinho[numbers][posQuad]
                                                y = round(x % 1, 1)
                                                x = round(x - 0.5)
                                                y = round(y*10)
                                                if matriz[x][y] != 0:
                                                        matrizComparacao.append(matriz[x][y])

                        possibilidades[linha, coluna] = matrizComparacao

                        '''Adiciona ao resto da linha ou coluna um número que não pode ser, baseado na sequencia de um quadradinho'''

#print(matrizComparacao)
print(possibilidades)

# VERIFICA SE TEM O VALOR NA MATRIZ, PERCORRENDO CADA VETOR DENTRO DELA
#valor = 1
#if any(valor in vetor for vetor in matriz):
#        print("ainda não terminou")
#else:
#        print("n tem esse numero")


















