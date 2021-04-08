from banco import Banco
from lista import ListaExceptionL
from pilha import PilhaExceptionP
from fila import FilaExceptionF

banco = Banco('Caixa')

#Contas em Lista 

ident = 3
cpf = 345
saldo = 1500
banco.adicionar_conta_LIncio(ident, cpf, saldo)

ident = 2
cpf = 798
saldo = 1500
banco.adicionar_conta_LFim(ident, cpf, saldo)

ident = 10
cpf = 134
saldo = 1500
i = 1
banco.adicionar_conta_LMeio(i ,ident, cpf, saldo)

ident = 1
cpf = 1324
saldo = 1500
i = 2
banco.adicionar_conta_LMeio(i ,ident, cpf, saldo)

ident = 5
cpf = 1314
saldo = 1500
banco.adicionar_conta_LFim(ident, cpf, saldo)

#Contas em Pilha 
ident = 4
cpf = 481
saldo = 1500
banco.adicionar_conta_P(ident, cpf, saldo)

ident = 5
cpf = 975
saldo = 1500
banco.adicionar_conta_P(ident, cpf, saldo)

#Contas em Filas

ident = 6
cpf = 367
saldo = 1500
banco.adicionar_conta_F(ident, cpf, saldo)

ident = 7
cpf = 937
saldo = 1500
banco.adicionar_conta_F(ident, cpf, saldo)

opcao = 1

while opcao != 0:

    print('*'*45)
    print('               MENU')
    print('*'*45)
    print('Opção 1 = Cadastro de Conta')
    print('Opção 2 = Consulta de Contas')
    print('Opção 0 = SAIR')
    opcao = int(input('Digide a Opção escolhida: '))

    if opcao == 1:

        while opcao != 4:

            print('*'*45)
            print('        CADASTRO DE CONTA')
            print('*'*45)
            print('Opção 1 = Lista de Contas')
            print('Opção 2 = Pilha de Contas')
            print('Opção 3 = Fila de Contas')
            print('Opção 4 = VOLTAR')
            opcao = int(input('Digide a Opção escolhida: '))

            if opcao == 1:

                while opcao != 6:

                    print('*'*45)
                    print('        MENU DE CADASTRO')
                    print('*'*45)
                    print('Opção 1 = Tamanho da Lista')
                    print('Opção 2 = Adicionar')
                    print('Opcao 3 = Buscar')
                    print('Opção 4 = Remover')
                    print('Opção 5 = Mostrar Lista')
                    print('Opção 6 = VOLTAR')
                    opcao = int(input('Digide a Opção escolhida: '))

                    if opcao == 1:
                        print('*'*45)
                        print(f'        Lista com {banco.mostrar_tam_contasL()} objeto(s)') 
                        print('*'*45)

                    elif opcao == 2:

                        while opcao != 4:

                            print('*'*45)
                            print('                MENU ADICIONAR')
                            print('*'*45)
                            print('Opção 1 = No Inicio da Lista Vazia')
                            print('Opção 2 = No Fim da Lista')
                            print('Opção 3 = Escolher uma Posição')
                            print('Opção 4 = VOLTAR')
                            opcao = int(input('Digide a Opção escolhida: '))
                            
                            if opcao == 1:
                                print('*'*45)
                                print(f'             Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                print('*'*45)
                                idc = int(input('Digite o Id: '))
                                cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                                sa = int(input('Digite o Saldo: '))
                                banco.adicionar_conta_LIncio(idc, cp, sa) 
                                print(f'             Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                print('*'*45)
                                

                            elif opcao == 2:
                                try:
                                    print('*'*45)
                                    print(f'             Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                    print('*'*45)
                                    idc = int(input('Digite o Id: '))
                                    cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                                    sa = int(input('Digite o Saldo: '))
                                    banco.adicionar_conta_LFim(idc, cp, sa) 
                                    print('*'*45)
                                    print(f'           Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                    print('*'*45)
                                except ListaExceptionL as le:    
                                    print(le)

                            elif opcao == 3:
                                try: 
                                    print('*'*45)
                                    print(f'             Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                    print('*'*45)
                                    idc = int(input('Digite o Id: '))
                                    cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                                    sa = int(input('Digite o Saldo: '))
                                    ind = int(input('Digite a posição: ')) 
                                    banco.adicionar_conta_LMeio(ind, idc, cp, sa)
                                    print('*'*45)
                                    print(f'          Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                                    print('*'*45)
                                except ListaExceptionL as le:  
                                    print(le)

                    elif opcao == 3:
                        print('*'*45)
                        try: 
                            id = int(input('Informe o Id para pesquisar: '))
                            #position = int(input('Digite a posicição: '))
                            print(banco.buscar_conta(id))
                        except ListaExceptionL as le:  
                            print(le)
                        print('*'*45)

                    elif opcao == 4:
                        try:
                            print('*'*45)
                            print(f'         Lista com {banco.mostrar_tam_contasL()} objeto(s).') 
                            id = int(input('Informe o Id a remover: ')) 
                            banco.remover_conta_L(id)
                            print(f'         Lista com {banco.mostrar_tam_contasL()} objeto(s).')
                        except ListaExceptionL as le:  
                            print(le)
                        print('*'*45)

                    elif opcao == 5:
                        print('*'*45)
                        print(f'{banco.imprimir_contasL()}') 
                        print('*'*45)

                    elif opcao == 6:
                        pass

            elif opcao == 2:

                    while opcao != 5:

                        print('*'* 45)
                        print('        MENU DE CADASTRO')
                        print('*'* 45)
                        print('Opção 1 = Tamanho da Pilha')
                        print('Opção 2 = Adicionar')
                        print('Opção 3 = Remover')
                        print('Opção 4 = Mostrar Pilha')
                        print('Opção 5 = Voltar')
                        opcao = int(input('Digide a Opção escolhida: '))

                        if opcao == 1:
                            print('*'*45)
                            print(f'        Pilha com {banco.mostrar_tam_contasP()} objeto(s)') 
                            print('*'*45)

                        elif opcao == 2:
                            print('*'*45)
                            print(f'             Pilha com {banco.mostrar_tam_contasL()} objeto(s).')
                            print('*'*45)
                            idc = int(input('Digite o Id: '))
                            cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                            sa = int(input('Digite o Saldo: '))
                            banco.adicionar_conta_P(idc, cp, sa)
                            print('*'*45)
                            print(f'          Pilha com {banco.mostrar_tam_contasP()} objeto(s).')
                            print('*'*45)

                        elif opcao == 3:

                            try:
                                print('*'*45)
                                print(f'         Pilha com {banco.mostrar_tam_contasP()} objeto(s).') 
                                a = input('Deseja remover a ultima conta ? ').upper()
                                if a == 'SIM' or a == 'S' or a == 'Yes':
                                    banco.remover_conta_P()
                                    print(f'        Pilha com {banco.mostrar_tam_contasP()} objeto(s).')
                            except PilhaExceptionP as le:  
                                print(le)
                            print('*'*45)
                        
                        elif opcao == 4:
                            print('*'*45)
                            print(f'         {banco.imprimir_contaP()}') 
                            print('*'*45)

            elif opcao == 3:
                while opcao != 5:

                        print('*'* 45)
                        print('        MENU DE CADASTRO')
                        print('*'* 45)
                        print('Opção 1 = Tamanho da Fila')
                        print('Opção 2 = Adicionar')
                        print('Opção 3 = Remover')
                        print('Opção 4 = Mostrar Fila')
                        print('Opção 5 = Voltar')
                        opcao = int(input('Digide a Opção escolhida: '))

                        if opcao == 1:
                            print('*'*45)
                            print(f'        Lista com {banco.mostrar_tam_contasF()} objeto(s)') 
                            print('*'*45)

                        elif opcao == 2:
                            print('*'*45)
                            print(f'             Lista com {banco.mostrar_tam_contasF()} objeto(s).')
                            print('*'*45)
                            idc = int(input('Digite o Id: '))
                            cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                            sa = int(input('Digite o Saldo: '))
                            banco.adicionar_conta_F(idc, cp, sa)
                            print('*'*45)
                            print(f'          Lista com {banco.mostrar_tam_contasF()} objeto(s).')
                            print('*'*45)

                        elif opcao == 3:

                            try:
                                print('*'*45)
                                print(f'         Pilha com {banco.mostrar_tam_contasF()} objeto(s).') 
                                a = input('Deseja remover o ultima conta ? ').upper()
                                if a == 'SIM' or a == 'S' or a == 'Yes':
                                    banco.remover_conta_F()
                                    print(f'        Pilha com {banco.mostrar_tam_contasF()} objeto(s).')
                            except FilaExceptionF as le:  
                                print(le)
                            print('*'*45)
                        
                        elif opcao == 4:
                            print('*'*45)
                            print(f'         {banco.imprimir_contaF()}') 
                            print('*'*45)

    elif opcao == 2:

        while opcao != 4:

            print('*'*45)
            print('        CONSULTA DE CONTAS')
            print('*'*45)
            print('Opção 1 = Lista de Contas')
            print('Opção 2 = Pilha de Contas')
            print('Opção 3 = Fila de Contas')
            print('Opção 4 = VOLTAR')
            opcao = int(input('Digide a Opção escolhida: '))

            if opcao == 1:
                
                while opcao != 10:

                    print('*'*45)
                    print('        CONSULTA DA LISTA')
                    print('*'*45)
                    print('Opção 1 = Tamanho da Lista')
                    print('Opção 2 = Busca')
                    print('Opção 3 = Mostrar Elemento')
                    print('Opção 4 = Ordenar Crescente')
                    print('Opção 5 = Ordenar Decrescente')
                    print('Opção 6 = Mostrar lista')
                    print('Opção 7 = Mostrar valor total das contas lista')
                    print('Opção 8 = Creditar valor na conta')
                    print('Opção 9 = Debitar valor na conta')
                    print('Opção 10 = Voltar')
                    opcao = int(input('Digide a Opção escolhida: '))

                    if opcao == 1:
                        print('*'*45)
                        print(f'        Lista com {banco.mostrar_tam_contasL()} objeto(s)') 
                        print('*'*45)

                    elif opcao == 2:
                        print('*'*45)
                        try: 
                            id = int(input('Informe o Id para pesquisar: '))
                            #position = int(input('Digite a posição para pesquisar: '))
                            print(banco.buscar_conta(id))
                            
                        except ListaExceptionL as le:  
                            print(le)
                        print('*'*45)

                    elif opcao == 3:
                        
                        while opcao != 4:

                            print('*'*45)
                            print('        CONSULTA POR ELEMENTO')
                            print('*'*45)
                            print('Opção 1 = Mostrar Id')
                            print('Opção 2 = Mostrar CPF')
                            print('Opção 3 = Mostrar Saldo')
                            print('Opção 4 = VOLTAR')
                            opcao = int(input('Digide a Opção escolhida: '))

                            if opcao == 1:
                                ind = int(input('Informe a posição: '))
                                print('*'*45)
                                print(f'Id: {banco.buscar_valor(ind).identificador}')
                                print('*'*45)

                            elif opcao == 2:
                                ind = int(input('Informe a posição: '))
                                print('*'*45)
                                print(f'Cpf: {banco.buscar_valor(ind).cpf}')
                                print('*'*45)

                            elif opcao == 3:
                                ind = int(input('Informe a posição: '))
                                print('*'*45)
                                print(f'Saldo: {banco.buscar_valor(ind).saldo}')
                                print('*'*45)


                    elif opcao == 4:
                        print('_'*17 + 'LISTA ANTES' + '_'*17)
                        print()
                        print(banco.imprimir_contasL())
                        banco.ordena_contasCrescente()
                        print('_'*15 + 'LISTA ATUALIZADA' + '_'*15)
                        print()
                        print(banco.imprimir_contasL())
                        

                    elif opcao  == 5:
                        print('_'*17 + 'LISTA ANTES' + '_'*17)
                        print()
                        print(banco.imprimir_contasL())
                        banco.ordena_contasDecrescente()
                        print('_'*15 + 'LISTA ATUALIZADA' + '_'*15)
                        print()
                        print(banco.imprimir_contasL())
                    
                    elif opcao == 6:
                        print('*'*45)
                        print(f'{banco.imprimir_contasL()}') 
                        print('*'*45)
                    
                    elif opcao == 7:
                        print('*'*45)
                        print(f'         Valor total das contas:{banco.total_valor_contas()}') 
                        print('*'*45)
                    
                    elif opcao == 8:
                        print('*'*45)
                        ident = int(input('Id da conta a ser creditado o valor: '))
                        valor = int(input('Digite o valor a ser creditado em sua conta: '))
                        print (banco.adicionar_valor_conta(ident, valor))
                        print('*'*45)
                    
                    elif opcao == 9:
                        print('*'*45)
                        ident = int(input('Id da conta a ser debitado o valor: '))
                        valor = int(input('Digite o valor a ser debitado da sua conta: '))
                        print (banco.retirar_valor_conta(ident, valor))
                        print('*'*45)

            elif opcao == 2:

                while opcao != 5:
                    print('*'*45)
                    print('        CONSULTA DA PILHA')
                    print('*'*45)
                    print('Opção 1 = Tamanho da Pilha')
                    print('Opção 2 = Mostrar Elemento')
                    print('Opção 3 = Modificar')
                    print('Opção 4 = Mostrar Pilha')
                    print('Opção 5 = voltar')
                    opcao = int(input('Digide a Opção escolhida: '))

                    if opcao == 1:
                        print('*'*45)
                        print(f'Pilha com {banco.mostrar_tam_contasP()} objeto(s)') 
                        print('*'*45)
                    
                    elif opcao == 2:

                        while opcao != 4:

                            print('*'*45)
                            print('        CONSULTA POR ELEMENTO')
                            print('*'*45)
                            print('Opção 1 = Mostrar Id')
                            print('Opção 2 = Mostrar CPF')
                            print('Opção 3 = Mostrar Saldo')
                            print('Opção 4 = VOLTAR')
                            opcao = int(input('Digide a Opção escolhida: '))

                            if opcao == 1:
                                print('*'*45)
                                print(f'Id: {banco.mostrar_elementP().identificador}')
                                print('*'*45)
                            
                            elif opcao == 2:
                                print('*'*45)
                                print(f'Cpf: {banco.mostrar_elementP().cpf}')
                                print('*'*45)
                            
                            elif opcao == 3:
                                print('*'*45)
                                print(f'Saldo: {banco.mostrar_elementP().saldo}')
                                print('*'*45)
                            
                    
                    elif opcao == 3:
                        print('*'*45)
                        idc = int(input('Digite o Id: '))
                        cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                        sa = int(input('Digite o Saldo: '))
                        print(banco.modificarP(idc, cp, sa))
                        print('*'*45)

                    elif opcao == 4:
                            print('*'*45)
                            print(f'         {banco.imprimir_contaP()}') 
                            print('*'*45)

            elif opcao == 3:
                while opcao != 5:
                    print('*'*45)
                    print('        CONSULTA DA FILA')
                    print('*'*45)
                    print('Opção 1 = Tamanho da Pilha')
                    print('Opção 2 = Mostrar Elemento')
                    print('Opção 3 = Modificar')
                    print('Opção 4 = Mostrar Fila')
                    print('Opção 5 = voltar')
                    opcao = int(input('Digide a Opção escolhida: '))

                    if opcao == 1:
                        print('*'*45)
                        print(f'Fila com {banco.mostrar_tam_contasF()} objeto(s)') 
                        print('*'*45)
                    
                    elif opcao == 2:

                        while opcao!= 5:
                            print('*'*45)
                            print('        CONSULTA POR ELEMENTO')
                            print('*'*45)
                            print('Opção 1 = Mostrar Id')
                            print('Opção 2 = Mostrar CPF')
                            print('Opção 3 = Mostrar Saldo')
                            print('Opção 4 = VOLTAR')
                            opcao = int(input('Digide a Opção escolhida: '))

                            if opcao == 1:
                                print('*'*45)
                                print(f'Id: {banco.mostrar_elementF().identificador}')
                                print('*'*45)
                            
                            elif opcao == 2:
                                print('*'*45)
                                print(f'Cpf: {banco.mostrar_elementF().cpf}')
                                print('*'*45)
                            
                            elif opcao == 3:
                                print('*'*45)
                                print(f'Saldo: {banco.mostrar_elementF().saldo}')
                                print('*'*45)
                            

                            elif opcao == 4:
                                opcao = 0
                                break
                        
                    elif opcao == 3:
                        print('*'*45)
                        idc = int(input('Digite o Id: '))
                        cp = input('Digite o CPF(xxx.xxx.xxx-xx): ')
                        sa = int(input('Digite o Saldo: '))
                        print(banco.modificarF(idc, cp, sa))
                        print('*'*45)
                    
                    elif opcao == 4:
                            print('*'*45)
                            print(f'         {banco.imprimir_contaF()}') 
                            print('*'*45)

    elif opcao == 0:
        print('Acesso encerrado')

