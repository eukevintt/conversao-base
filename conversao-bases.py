continuar = 's'
while continuar == 's':
    print('Escolha entre uma das opções: \n 1 - Converter de decimal para binário \n 2 - Converter de binário para decimal')
    escolha = input('Escolha o número que deseja: ')
    if escolha == '1':
            def toBaseBi(num):
                """
                    Função que converte um número decimal para binário.

                    Args:
                        num: Número em decimal, que seja inteiro.

                    Return:
                        Retorna um número em binário

                    int -> int
                """
                rest2 = num % 2
                final = [rest2]
                while num > 1:
                    num = num // 2
                    rest = num % 2
                    final.insert(0, rest)
                print('O número decimal '+str(numEscolha)+' em binário é', end=' ')
                print(*final, sep="")
            numEscolha = input("Diga um número em decimal que seja inteiro: ")
            toBaseBi(int(numEscolha))
            continuar = input('Deseja continuar?(s/n): ').lower()
    elif escolha == '2':
        def toBaseTen(num):
            """
                Função que converte um número binário para decimal.

                Args:
                    num: Número em binário.

                Returns:
                    Retorna um número inteiro em decimal.

                int -> int
            """
            tamanho = len(str(num))
            i = 0
            num2 = 0
            lista = list(str(num))
            lista.reverse()
            while tamanho > i:
                num = int(lista[i]) * 2 ** i
                num2 = num + num2
                i = i + 1
            print('O número binário '+str(numEscolha)+' em decimal é '+str(num2))
        numEscolha = input("Diga um número em binário: ")
        toBaseTen(int(numEscolha))
        continuar = input('Deseja continuar?(s/n): ').lower()
else:
    print('Até mais :)')