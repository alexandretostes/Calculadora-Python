n1 = float(input('Digente um valor: '))
n2 = float(input('Digente outro valor: '))
print("**********************************")
print('Para somar digite -> S')
print('Para subtrair digite -> SUB')
print('Para dividir digite -> D')
print('Para multiplicar digite -> M')
print('Para exponencializar digite -> E')
print("**********************************")
operacao = input('Digite a operação que deseja realizar: ') .upper()
if(n2 == 0 and operacao == 'D'):
    print('Não é possivel realizado divisão, pois não da pra dividir {:.0f} por 0'.format(n1))
    exit()


if (operacao != 'S' and operacao != 'SUB' and operacao != 'D' and operacao != 'M' and operacao != 'E'):
    print('Você não escolheu uma operação valida!')
    exit()


def calculadora():
    if (operacao == 'S'):
        soma = n1 + n2
        print("++++++++++++++++++++++++++++++++++")
        print('A soma é {:.0f}'.format(soma))
        print("++++++++++++++++++++++++++++++++++")
    elif (operacao == 'SUB'):
        subtracao = n1 - n2
        print("----------------------------------")
        print('A subtração é {:.0f}'.format(subtracao))
        print("----------------------------------")
    elif (operacao == 'D'):
        divisao = n1 / n2
        print("//////////////////////////////////")
        print('A divisão é {:.0f}'.format(divisao))
        print("//////////////////////////////////")
    elif (operacao == 'M'):
        multi = n1 * n2
        print("**********************************")
        print('A multiplicação é {:.0f}'.format(multi))
        print("**********************************")
    elif (operacao == 'E'):
        expo = n1 ** n2
        print("**********************************")
        print('A expotenciação é {:.0f}'.format(expo))
        print("**********************************")



calculadora()


