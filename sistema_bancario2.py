def menu():
    menu = '''\n
    ************** MENU **************

             [s] - Sacar
             [d] - Depositar
             [e] - Extrato
            [nc] - Nova conta
            [lc] - Listar contas
            [nu] - Novo usuário
             [q] - Sair

    **********************************
    -> '''
    return input(menu).lower()

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques <= limite_saques:
        if valor <= limite:
            if saldo >= valor:
                saldo -= valor
                numero_saques+=1
                extrato += f'\tSaque:\t\tR$ {valor:,.2f}\n'
                print('\nFavor retirar o dinheiro')
            else:
                print('Falha no processamento da operação: O saldo atual é insuficiente para realizar a operação.')
        else:
            print('Falha no processamento da operação: O valor do saque excede o limite permitido.')
    else:
        print('Falha no processamento da operação: A quantidade máxima de saques foi excedida.')
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'\tDepósito:\tR$ {valor:,.2f}\n'
    else:
        print('Erro: Informe um valor válido para depositar.')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f'\n*************** EXTRATO ***************')
    print(f'\tNão foram realizadas movimentações.' if not extrato else extrato)
    print(f'\n\tSaldo:\t\tR$ {saldo:,.2f}')
    print(f'*****************************************')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe um usuário com o CPF informado.')
        return

    nome = input('Informe seu nome completo: ')
    data_de_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): ')
    
    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print(f'\nUsuário não encontrado, processo de criação de conta encerrado.')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 60)
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3

    AGENCIA = '0001'
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input('\nInforme o valor que deseja depositar: R$ '))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == 's':
            valor = float(input('\nInforme o valor que deseja sacar: R$ '))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
                
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao =='nu':
            criar_usuario(usuarios)
    
        elif opcao == 'nc':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
                
            if conta:
                contas.append(conta)
                numero_conta += 1
    
        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == 'q':
            break
        
        else:
            print('Opção inválida, favor selecione novamente a opção desejada')
main()
