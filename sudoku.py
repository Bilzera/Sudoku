matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

""" ------------------ PRÉ PREENCHIMENTO DA MATRIZ ------------------ """

linha = 10
posicao = 10
prenumero = 10

print("Antes do Sudoku ser solucionado, vamos preencher os números pré estabelecidos")

while linha != 0:
    linha = int(input("Digite a linha de 1 a 9 que deseja preencher, se estiver tudo certo para resolver o sudoku, digite 0: "))
    if linha > 9 or linha < 0:
        print("Você digitou um número diferente de 1 a 9, por favor escolha uma linha de 1 a 9 ou digite 0 caso tenha finalizado")
    elif linha == 0:
        print(matriz)
        print("Sua matriz ficou da seguinte maneira, deseja que essa matriz seja resolvida?")
    else:
        while posicao > 9 or posicao < 1:
            posicao = int(input("Agora digite a posição de 1 a 9 da linha escolhida: "))
            if posicao > 9 or posicao < 1:
                print("Você digitou um número diferente de 1 a 9, por favor escolha uma posição valida")
            else:
                while prenumero > 9 or prenumero < 1:
                    prenumero = int(input("Agora que sabemos a linha e posição que deseja alterar, por favor insira o número de 1 a 9 pré estabelecido pelo exercício: "))
                    if prenumero > 9 or prenumero < 1:
                        print("Você digitou um número invalido, no sudoku só existem números de 1 a 9")
                    else:
                        matriz[linha - 1][posicao - 1] = prenumero
                        print("Sua matriz parcial está da seguinte maneira")
                        print()
                        
                        for linha in range (0, 9):
                            for coluna in range (0, 9):
                                print(f'[{matriz[linha][coluna]}]', end = "")
                            print()
                        print("\n")
    linha = 10
    posicao = 10
    prenumero = 10

""" ------------------ PRÉ PREENCHIMENTO DA MATRIZ ------------------ """      
    
                

''' ATÉ AQUI ESTÁ CERTO
for linha in range (0, 9):
        for coluna in range (0, 9):
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
                possibilidades[linha, coluna] = matrizComparacao
'''
