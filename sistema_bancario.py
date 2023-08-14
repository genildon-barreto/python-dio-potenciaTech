menu = '''
[s] - Sacar
[d] - Depositar
[e] - Extrato
[q] - Sair

-> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor que deseja depositar: R$ '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:,.2f}\n'
        else:
            print('Erro: Informe um valor válido para depositar.')
        
    elif opcao == 's':
        print('Informe o valor que deseja sacar: R$')
        valor = float(input())
        if numero_saques <= LIMITE_SAQUES:
            if valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    numero_saques+=1
                    extrato += f'Saque: R$ {valor:,.2f}\n'
                    print('Favor retirar o dinheiro')
                else:
                    print('Falha no processamento da operação: O saldo atual é insuficiente para realizar a operação.')
            else:
                print('Falha no processamento da operação: O valor do saque excede o limite permitido.')
        else:
            print('Falha no processamento da operação: A quantidade máxima de saques foi excedida.')
            
    elif opcao == 'e':
        print(f'\n******************* EXTRATO *******************')
        print(f'Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:,.2f}')
        print(f'*************************************************')
        
    elif opcao == 'q':
        break
    
    else:
        print('Opção inválida, favor selecione novamente a opção desejada')