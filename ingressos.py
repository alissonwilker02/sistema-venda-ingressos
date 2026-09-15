#/*******************************************************************************
#Autor: Alisson Wilker Santos Costa
#Componente Curricular: MI-Algoritmos
#Concluido em: 19/04/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************\

soma_idade_int = 0 #SOMA DE IDADES INGRESSO INTEIRO
qtd_idade_int = 0 #CONTADOR DE IDADES INGRESSO INTEIRO
soma_idade_meia = 0 #SOMA DE IDADES MEIA ENTRADA
qtd_idade_meia = 0 #CONTADOR DE IDADES MEIA ENTRADA
soma_idade_desconto = 0 #SOMA DE IDADES INGRESSO COM DESCONTO
qtd_idade_desconto = 0 #CONTADOR DE IDADES INGRESSO COM DESCONTO
soma_idade_cortesia = 0 #SOMA DE IDADES CORTESIA
qtd_idade_cortesia = 0 #CONTADOR DE IDADES CORTESIA
ingressos_comprados = 0 #VALOR TOTAL DE INGRESSOS COMPRADOS
quantcomissao = 0 #CONTADOR DE COMISSÃO
contrecebe = 0 #QUANTIDADE DE INGRESSOS PARA CHEGAR A META COMISSIONADA
recebe = 0 #CÁLCULO DA QUANTIDADE DE COMISSÕES
recebe2 = 0 #CÁLCULO DA QUANTIDADE DE COMISSÕES
estudante = 0 #COMPROVAÇÃO MEIA ENTRADA
idoso = 0 #COMPROVAÇÃO MEIA ENTRADA
outro = 0 #COMPROVAÇÃO MEIA ENTRADA
numero_cortesias = 0 #NÚMERO DE CORTESIAS
cortesias_restantes = 0 #CÁLCULA AS CORTESIAS RESTANTES
ingressos_comissionados = 0 #ACUMULA OS INGRESSOS COMISSIONADOS
guardacomissao = 0
acumulucroint = 0 # acumulador de lucro comum
acumulucroint1 = 0 # acumulador de lucro comissionado 1
acumulucroint2 = 0 # acumulador de lucro comissionado 2
acumulucromeia = 0 # acumulador de lucro meia comum
acumulucromeia1 = 0 # acumulador de lucro meia comissionado 1
acumulucromeia2 = 0 # acumulador de lucro meia comissionado 2
acumulucrodesc = 0 # acumulador de lucro desconto comum
acumulucrodesc1 = 0 # acumulador de lucro desconto comissionado 1
acumulucrodesc2 = 0 # acumulador de lucro desconto comissionado 2
resto = 0
contint = 0
contmeia = 0
contdesc = 0
contcort = 0
contint1 = 0
contmeia1 = 0
contdesc1 = 0
contcort1 = 0
contint2 = 0
contmeia2 = 0
contdesc2 = 0
contcort2 = 0

a = True #WHILE DAS CONFIGURAÇÕES
b = True #while dos ingressos disponíveis
d = True #while meia entrada
e = True #while comissão
f = True #while desconto
g = True #while cortesia
h = True #while voltar configuração
i = True #WHILE DAS VENDAS
j = True #while vendedores
k = True

#INTRODUÇÃO AO SISTEMA:
print('=-' * 40)
print(' ' * 20, 'SISTEMA DE VENDA DE INGRESSOS', ' ' * 20)
print('=-' * 40)
print('OLÁ!\nVamos fazer suas primeiras configurações?')#recepção ao usuário
prosseguir = bool(input('pressione ENTER para prosseguir...\n'))
while a == True:
    a = True  # WHILE DAS CONFIGURAÇÕES
    b = True  # while dos ingressos disponíveis
    c = True  # while do valor do ingresso
    d = True  # while meia entrada
    e = True  # while comissão
    f = True  # while desconto
    g = True  # while cortesia
    h = True  # while voltar configuração
    i = True  # WHILE DAS VENDAS
    j = True  # while vendedores


    # 1-COMEÇO DAS CONFIGURAÇÕES:
    while b == True: # O usúario não consegue seguir até digitar um valor válido
        print('MENU DE CONFIGURAÇÕES:')
        # b-) Valor total de ingressos:
        ingressos_disponiveis = input('Quantidade de ingressos disponíveis:').strip()
        if ingressos_disponiveis.isdigit():
            ingressos_disponiveis = int(ingressos_disponiveis)
            b = False # permite o usuário prosseguir no sistema
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


    # c-) Valor do ingresso:
    valor_ingresso = input('Valor do ingresso: R$').strip()
    while not valor_ingresso.replace('.','').isdigit():
        print('DÍGITO INVÁLIDO!\nTente novamente...')
        print('=-' * 20)
        valor_ingresso = input('Valor do ingresso: R$').strip()
    valor_ingresso = float(valor_ingresso)


    # d-) Meia entrada:
    while d == True: # O usúario não consegue seguir até digitar um valor válido
        print('[ 1 ] SIM')
        print('[ 2 ] NÃO')
        meia_entrada = input('Haverá meia entrada?').strip()
        if meia_entrada.isdigit():
            meia_entrada = int(meia_entrada)
            if meia_entrada == 1 or meia_entrada == 2:
                d = False # permite o usuário prosseguir no sistema
                print('OK!')
                print('=-' * 20)
            else:
                print('OPÇÃO INVÁLIDA!\nTente novamente...')
                print('=-' * 20)
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


    #e-) Comissão:
    while e == True: # O usúario não consegue seguir até digitar um valor válido
        print('[ 1 ] SIM')
        print('[ 2 ] NÃO')
        comissao = input('Haverá grupos de vendedores comissionados?').strip()
        if comissao.isdigit():
            comissao = int(comissao)
            if comissao == 1: #Grupos da comissão
                grupo1 = input('MÁXIMO DE 2 GRUPOS!\nDigite o nome do 1° grupo:').strip() #restringe uma quantidade de grupos
                grupo2 = input('Digite o nome do 2° grupo:').strip()
                print('Grupos registrados: {} e {}'.format(grupo1, grupo2))
                ingcomissao = input('A cada quantos ingressos vendidos o grupo terá um ingresso comissionado?').strip()
                if ingcomissao.isdigit():
                    ingcomissao = int(ingcomissao)
                    print('=-' * 20)
                    e = False # permite o usuário prosseguir no sistema
                else:
                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                    print('=-' * 20)
            elif comissao == 2:
                print('OK!')
                print('=-' * 20)
                e = False # permite o usuário prosseguir no sistema
            else:
                print('OPÇÃO INVÁLIDA!\nTente novamente...')
                print('=-' * 20)
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


    # f-) desconto:
    while f == True: # O usúario não consegue seguir até digitar um valor válido
        print('[ 1 ] SIM')
        print('[ 2 ] NÃO')
        desconto = input('Haverá descontos especiais?').strip()
        if desconto.isdigit():
            desconto = int(desconto)
            if desconto == 1:
                valor_desconto = input('Valor do ingresso com desconto: R$').strip()# valor final com desconto
                while not valor_desconto.replace('.', '').isdigit():
                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                    print('=-' * 20)
                    valor_desconto = input('Valor do ingresso com desconto: R$').strip()  # valor final com desconto
                valor_desconto = float(valor_desconto)
                grupodesconto = input('Nome do grupo que receberá desconto:').strip()# grupo com desconto
                print('=-' * 20)
                f = False # permite o usuário prosseguir no sistema
            elif desconto == 2:
                print('OK!')
                print('=-' * 20)
                f = False # permite o usuário prosseguir no sistema
            else:
                print('OPÇÃO INVÁLIDA,\ntente novamente...')
                print('=-' * 20)  # separando as informações
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


    # g-) Cortesia:
    while g == True: # O usúario não consegue seguir até digitar um valor válido
        print('[ 1 ] SIM')
        print('[ 2 ] NÃO')
        cortesia = input('Haverá ingressos gratuitos/cortesias?').strip()
        if cortesia.isdigit():
            cortesia = int(cortesia)
            if cortesia == 1:
                grupocortesia = input('Nome do grupo que receberá a cortesia:')# grupo que terá a cortesia
                print('Grupo {} registrado'.format(grupocortesia))
                numero_cortesias = input('Número de ingressos gratuitos:') # delimita uma quantidade de ingressos gratuitos
                if numero_cortesias.isdigit():
                    numero_cortesias = int(numero_cortesias)
                    print('=-' * 20)
                    print('\nTUDO PRONTO! CONFIGURAÇÃO FINALIZADA!\n') # Fim das configurações iniciais
                    g = False # permite o usuário prosseguir no sistema
                else:
                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                    print('=-' * 20)
            elif cortesia == 2:
                print('OK!')
                print('=-' * 20)
                print('\nTUDO PRONTO! CONFIGURAÇÃO FINALIZADA!\n')
                g = False # permite o usuário prosseguir no sistema
            else:
                print('OPÇÃO INVÁLIDA!\nTente novamente...')
                print('=-' * 20)
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


    #configurar novamente ou prosseguir:
    while h == True:
        print('[ 1 ] CONFIGURAR NOVAMENTE')
        print('[ 2 ] MENU DE VENDAS')
        opcao = input('Digite a opção:').strip()
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                print('=-' * 20)
                h = False # permite o usuário prosseguir no sistema
            elif opcao == 2:
                a = False # permite o usuário prosseguir no sistema
                h = False # permite o usuário prosseguir no sistema
            else:
                print('OPÇÃO INVÁLIDA!\nTente novamente...')
                print('=-' * 20)
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)


#2-Começo das vendas:
print('=-' * 40)
print(' ' * 20, 'MENU DE VENDAS:', ' ' * 20)
print('=-' * 40)
while i == True:
# Nessa parte é possível escolher o vendedor e o tipo de ingresso solicitado pelo cliente


    #escolher vendedor:
    while j == True: # O usúario não consegue seguir até digitar um valor válido
        ingressos_restantes = ingressos_disponiveis - ingressos_comprados - numero_cortesias - ingressos_comissionados#ingressos que estão dísponiveis para a VENDA
        print('INGRESSOS DISPONÍVEIS PARA A VENDA: {}/{}'.format(ingressos_restantes, ingressos_disponiveis))
        print('CORTESIAS DISPONÍVEIS: {}/{}'.format(numero_cortesias - cortesias_restantes, numero_cortesias)) #Cortesias que restam
        if ingressos_comissionados >= 1:
            # se os ingressos comissionados atingirem 1, aparece na tela as comissoes
            print('QUANTIDADE DE COMISSÕES JÁ DÍPONÍVEIS: {}'.format(ingressos_comissionados))

        #selecionar o tipo de vendedor ou encerrar
        print('=-' * 20)
        print('[ 1 ] VENDEDOR COMUM')
        print('[ 2 ] VENDEDOR COMISSIONADO')
        print('[ 3 ] ENCERRAR E VER RELATÓRIO')
        vendas = input('Selecione o tipo de vendedor:')
        print('=-' * 20)
        if vendas.isdigit():
            vendas = int(vendas)

            #selecionar o tipo de ingresso
            if vendas == 1:
                print('ABA DE VENDAS:\nvendedor comum:')
                print('[ 1 ] INTEIRA')
                print('[ 2 ] MEIA ENTRADA')
                print('[ 3 ] DESCONTO')
                print('[ 4 ] CORTESIA')
                print('[ 5 ] PARAR DE VENDER ')
                vendedor_comum = input('Digite a opção:')
                if vendedor_comum.isdigit():
                    vendedor_comum = int(vendedor_comum)


                    #VENDEDOR COMUM INTEIRA:
                    if vendedor_comum == 1:
                        print('Esse ingresso custa R${}'.format(valor_ingresso))
                        quantidade_inteira = input('Quantidade de ingressos que serão vendidos:') #venda de qualquer quantidade de acordo com os ingressos disponíveis
                        if quantidade_inteira.isdigit():
                            quantidade_inteira = int(quantidade_inteira)
                            if quantidade_inteira <= ingressos_restantes: #limite para não ultrapassar o limite de ingressos restantes
                                print('{} Ingresso(s) vendido(s)'.format(quantidade_inteira))
                                lucro_int = quantidade_inteira * valor_ingresso #Mostra a arrecadação
                                acumulucroint += lucro_int
                                print('Arrecadação de: R${}'.format(lucro_int))
                                ingressos_comprados += quantidade_inteira #acumulador de ingressos comprados
                                contint += quantidade_inteira
                                for i in range(1, quantidade_inteira + 1):
                                    idade_int = input('Digite a idade do {}° comprador:'.format(i)) #idade dos compradores
                                    while not idade_int.isdigit() or idade_int == '':
                                        idade_int = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                    idade_int = int(idade_int)
                                    soma_idade_int += idade_int
                                    qtd_idade_int += 1
                            else: #impede ultrapassar o limite de ingressos
                                print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))


                   #VENDEDOR COMUM MEIA ENTRADA:
                    elif vendedor_comum == 2:
                        if meia_entrada == 1: #Usuário deve ter confirmado essa opção na configuração
                            print('Esse ingresso custa R${}'.format(valor_ingresso / 2))
                            quantidade_meia = input('Quantidade de ingressos que serão vendidos:')#venda de qualquer quantidade de acordo com os ingressos disponíveis
                            if quantidade_meia.isdigit():
                                quantidade_meia = int(quantidade_meia)
                                if quantidade_meia <= ingressos_restantes:#limite para não ultrapassar o limite de ingressos restantes
                                    print('{} Ingresso(s) vendido(s)'.format(quantidade_meia))
                                    lucro_meia = quantidade_meia * (valor_ingresso / 2) #Mostra a arrecadação
                                    acumulucromeia += lucro_meia
                                    print('Arrecadação de: R${}'.format(lucro_meia))
                                    ingressos_comprados += quantidade_meia #acumulador de ingressos comprados
                                    contmeia += quantidade_meia
                                    #comprovação meia entrada
                                    for p in range(1, quantidade_meia + 1):
                                        print('Selecione o tipo de comprovação para a {}° meia entrada:'.format(p)) #comprovação para a meia entrada
                                        opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                        while k == True:
                                            if opcao2.isdigit():
                                                opcao2 = int(opcao2)
                                                if opcao2 == 1:
                                                    estudante += 1  # opção estudante
                                                    print('comprovação cadastrada!\n')
                                                    k = False
                                                elif opcao2 == 2:
                                                    idoso += 1  # opção idoso
                                                    print('comprovação cadastrada!\n')
                                                    k = False
                                                elif opcao2 == 3:
                                                    outro += 1  # opção outro
                                                    print('comprovação cadastrada!\n')
                                                    k = False
                                                else:
                                                    print('OPÇÃO INVÁLIDA!\nTente novamente...')
                                                    print('=-' * 20)
                                                    print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                    opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                            else:
                                                print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                print('=-' * 20)
                                                print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                    #cadastrar idades
                                    for i in range(1, quantidade_meia + 1):
                                        idade_meia = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        while not idade_meia.isdigit() or idade_meia == '':
                                            idade_meia = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        idade_meia = int(idade_meia)
                                        soma_idade_meia += idade_meia
                                        qtd_idade_meia += 1
                                else: #impede ultrapassar o limite de ingressos
                                    print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))
                        else:
                            print('MEIA ENTRADA NÃO CADASTRADA!') #Quando é negada a opção nas configurações


                    #VENDEDOR COMUM DESCONTO:
                    elif vendedor_comum == 3:
                        if desconto == 1:  #Usuário deve ter confirmado essa opção na configuração
                            print('Esse ingresso custa R${}'.format(valor_desconto))
                            quantidade_desconto = input('Quantidade de ingressos que serão vendidos:')#venda de qualquer quantidade de acordo com os ingressos disponíveis
                            if quantidade_desconto.isdigit():
                                quantidade_desconto = int(quantidade_desconto)
                                if quantidade_desconto <= ingressos_restantes: #limite para não ultrapassar o limite de ingressos restantes
                                    print('{} Ingresso(s) vendido(s)'.format(quantidade_desconto))
                                    lucro_desconto = quantidade_desconto * valor_desconto #Mostra a arrecadação
                                    acumulucrodesc += lucro_desconto
                                    print('Arrecadação de: R${}'.format(lucro_desconto))
                                    ingressos_comprados += quantidade_desconto #acumulador de ingressos comprados
                                    contdesc += quantidade_desconto
                                    for i in range(1, quantidade_desconto + 1):
                                        idade_desconto = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        while not idade_desconto.isdigit() or idade_desconto == '':
                                            idade_desconto = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        idade_desconto = int(idade_desconto)
                                        soma_idade_desconto += idade_desconto
                                        qtd_idade_desconto += 1
                                else: #impede ultrapassar o limite de ingressos
                                    print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))
                        else: #Quando é negada a opção nas configurações
                            print('DESCONTO NÃO CADASTRADO!')


                   #VENDEDOR COMUM CORTESIA:
                    elif vendedor_comum == 4:
                        if cortesia == 1 and numero_cortesias <= numero_cortesias: #Usuário deve ter confirmado essa opção na configuração
                            print('Esse ingresso é gratuito')
                            quantidade_cortesia = input('Quantidade de ingressos que serão entregues:')
                            if quantidade_cortesia.isdigit():
                                quantidade_cortesia = int(quantidade_cortesia)
                                if quantidade_cortesia <= numero_cortesias - cortesias_restantes: #limite para não ultrapassar o limite de cortesias restantes
                                    print('{} Ingresso(s) entregue(s)'.format(quantidade_cortesia))
                                    contcort += quantidade_cortesia
                                    for i in range(1, quantidade_cortesia + 1):
                                        idade_cortesia = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        #cadastrar idades
                                        while not idade_cortesia.isdigit() or idade_cortesia == '':
                                            idade_cortesia = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                        idade_cortesia = int(idade_cortesia)
                                        soma_idade_cortesia += idade_cortesia
                                        qtd_idade_cortesia += 1
                                        cortesias_restantes += 1
                                else: #impede ultrapassar o limite de ingressos
                                    print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))
                        else: #Quando é negada a opção nas configurações
                            print('CORTESIA NÃO CADASTRADA!')


           #VENDEDOR COMISSIONADO:
            elif vendas == 2: #área do vendedor comissionado
                if comissao == 1:
                    print('[ 1 ] {}'.format(grupo1))
                    print('[ 2 ] {}'.format(grupo2))
                    escolha_comissao = input('Digite o seu grupo:')
                    if escolha_comissao.isdigit():
                        escolha_comissao = int(escolha_comissao)


                        #GRUPO DE COMISSÃO 1:
                        #selecionar o tipo de ingresso
                        if escolha_comissao == 1:
                            print('GRUPO DE COMISSÃO: {}\n'.format(grupo1))
                            print('ABA DE VENDAS:\nvendedor comissionado:')
                            print('[ 1 ] INTEIRA')
                            print('[ 2 ] MEIA ENTRADA')
                            print('[ 3 ] DESCONTO')
                            print('[ 4 ] CORTESIA')
                            print('[ 5 ] PARAR DE VENDER ')
                            #escolha de ingressos:
                            vendedor_comissionado = input('Digite a opção:')
                            if vendedor_comissionado.isdigit():
                                vendedor_comissionado = int(vendedor_comissionado)


                               #GRUPO 1 INTEIRA:
                                if vendedor_comissionado == 1:
                                    print('Esse ingresso custa R${}'.format(valor_ingresso))
                                    quantidade_inteira1 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_inteira1.isdigit():
                                        quantidade_inteira1 = int(quantidade_inteira1)
                                        if quantidade_inteira1 <= ingressos_restantes:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_inteira1))
                                            ingressos_comprados += quantidade_inteira1
                                            lucro_int1 = quantidade_inteira1 * valor_ingresso
                                            acumulucroint1 += lucro_int1
                                            print('Arrecadação de: R${}'.format(lucro_int1))
                                            contint1 += quantidade_inteira1
                                            #cadastrar idades
                                            for i in range(1, quantidade_inteira1 + 1):
                                                idade_int = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                                while not idade_int.isdigit() or idade_int == '':
                                                    idade_int = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                                idade_int = int(idade_int)
                                                soma_idade_int += idade_int
                                                qtd_idade_int += 1
                                            if quantidade_inteira1 >= ingcomissao:
                                                resultado = quantidade_inteira1 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_inteira1 < ingcomissao:
                                                resto += quantidade_inteira1
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))


                                #GRUPO 1 MEIA ENTRADA:
                                elif vendedor_comissionado == 2:
                                    print('Esse ingresso custa R${}'.format(valor_ingresso / 2))
                                    quantidade_meia1 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_meia1.isdigit():
                                        quantidade_meia1 = int(quantidade_meia1)
                                        if quantidade_meia1 <= ingressos_restantes:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_meia1))
                                            lucro_meia1 = quantidade_meia1 * (valor_ingresso / 2)
                                            acumulucromeia1 += lucro_meia1
                                            ingressos_comprados += quantidade_meia1
                                            contmeia1 += quantidade_meia1
                                            print('Arrecadação de: R${}'.format(lucro_meia1))
                                            #comprovação meia entrada
                                            for p in range(1, quantidade_meia1 + 1):
                                                print('Selecione o tipo de comprovação para a {}° meia entrada:'.format(p))  # comprovação para a meia entrada
                                                opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                                while k == True:
                                                    if opcao2.isdigit():
                                                        opcao2 = int(opcao2)
                                                        if opcao2 == 1:
                                                            estudante += 1  # opção estudante
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        elif opcao2 == 2:
                                                            idoso += 1  # opção idoso
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        elif opcao2 == 3:
                                                            outro += 1  # opção outro
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        else:
                                                            print('OPÇÃO INVÁLIDA!\nTente novamente...')
                                                            print('=-' * 20)
                                                            print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                            opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                                    else:
                                                        print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                        print('=-' * 20)
                                                        print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                        opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                            #cadastrar idades
                                            for m in range(1, quantidade_meia1 + 1):
                                                idade_meia = input('Digite a idade do {}° comprador:'.format(m))
                                                if idade_meia.isdigit():
                                                    idade_meia = int(idade_meia)
                                                    soma_idade_meia += idade_meia
                                                    qtd_idade_meia += 1
                                            if quantidade_meia1 >= ingcomissao:
                                                resultado = quantidade_meia1 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_meia1 < ingcomissao:
                                                resto += quantidade_meia1
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))
                                    else:
                                        print('DÍGITO INVÁLIDO!\nTente novamente...')
                                        print('=-' * 20)


                                #GRUPO 1 DESCONTO:
                                elif vendedor_comissionado == 3:
                                    print('Esse ingresso custa R${}'.format(valor_desconto))
                                    quantidade_desconto1 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_desconto1.isdigit():
                                        quantidade_desconto1 = int(quantidade_desconto1)
                                        if quantidade_desconto1 <= ingressos_restantes:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_desconto1))
                                            lucro_desconto1 = quantidade_desconto1 * valor_desconto
                                            acumulucrodesc1 += lucro_desconto1
                                            ingressos_comprados += quantidade_desconto1
                                            print('Arrecadação de: R${}'.format(lucro_desconto1))
                                            contdesc1 += quantidade_desconto1
                                            #cadastrar idades
                                            for d in range(1, quantidade_desconto1 + 1):
                                                idade_desconto = input('Digite a idade do {}° comprador:'.format(d))
                                                if idade_desconto.isdigit():
                                                    idade_desconto = int(idade_desconto)
                                                    soma_idade_desconto += idade_desconto
                                                    qtd_idade_desconto += 1
                                                else:
                                                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                    print('=-' * 20)
                                            if quantidade_desconto1 >= ingcomissao:
                                                resultado = quantidade_desconto1 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_desconto1 < ingcomissao:
                                                resto += quantidade_desconto1
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))


                                #GRUPO 1 CORTESIA:
                                elif vendedor_comissionado == 4 and cortesia == 1:
                                    print('Esse ingresso é gratuito'.format(valor_desconto))
                                    quantidade_cortesia1 = input('Quantidade de ingressos que serão entregues:')
                                    if quantidade_cortesia1.isdigit():
                                        quantidade_cortesia1 = int(quantidade_cortesia1)
                                        print('{} Ingresso(s) entregue(s)'.format(quantidade_cortesia1))
                                        contcort1 += quantidade_cortesia1
                                        if quantidade_cortesia1 <= numero_cortesias - cortesias_restantes:
                                            # cadastrar idades
                                            for c in range(1, quantidade_cortesia1 + 1):
                                                idade_cortesia = input('Digite a idade do {}° comprador:'.format(c))
                                                if idade_cortesia.isdigit():
                                                    idade_cortesia = int(idade_cortesia)
                                                    soma_idade_cortesia += idade_cortesia
                                                    qtd_idade_cortesia += 1
                                                    cortesias_restantes += 1
                                                else:
                                                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                    print('=-' * 20)
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(numero_cortesias - cortesias_restantes))


                         #grupo de comissao 2:
                        #selecionar o tipo de ingresso
                        elif escolha_comissao == 2:
                            print('GRUPO DE COMISSÃO: {}\n'.format(grupo2))
                            print('ABA DE VENDAS:\nvendedor comissionado:')
                            print('[ 1 ] INTEIRA')
                            print('[ 2 ] MEIA ENTRADA')
                            print('[ 3 ] DESCONTO')
                            print('[ 4 ] CORTESIA')
                            print('[ 5 ] PARAR DE VENDER ')
                            #escolha tipo de ingresso:
                            vendedor_comissionado2 = input('Digite a opção:')
                            if vendedor_comissionado2.isdigit():
                                vendedor_comissionado2 = int(vendedor_comissionado2)


                                #GRUPO 2 INTEIRA
                                if vendedor_comissionado2 == 1:
                                    print('Esse ingresso custa R${}'.format(valor_ingresso))
                                    quantidade_inteira2 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_inteira2.isdigit():
                                        quantidade_inteira2 = int(quantidade_inteira2)
                                        if quantidade_inteira2 <= ingressos_disponiveis:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_inteira2))
                                            ingressos_comprados += quantidade_inteira2
                                            lucro_int2 = quantidade_inteira2 * valor_ingresso
                                            acumulucroint2 += lucro_int2
                                            print('Arrecadação de: R${}'.format(lucro_int2))
                                            contint2 += quantidade_inteira2
                                            # cadastrar idades
                                            for i in range(1, quantidade_inteira2 + 1):
                                                idade_int = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                                while not idade_int.isdigit() or idade_int == '':
                                                    idade_int = input('Digite a idade do {}° comprador:'.format(i))  # idade dos compradores
                                                idade_int = int(idade_int)
                                                soma_idade_int += idade_int
                                                qtd_idade_int += 1
                                            if quantidade_inteira2 >= ingcomissao:
                                                resultado = quantidade_inteira2 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_inteira2 < ingcomissao:
                                                resto += quantidade_inteira2
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))


                                #GRUPO 2 MEIA ENTRADA:
                                elif vendedor_comissionado2 == 2:
                                    print('Esse ingresso custa R${}'.format(valor_ingresso / 2))
                                    quantidade_meia2 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_meia2.isdigit():
                                        quantidade_meia2 = int(quantidade_meia2)
                                        if quantidade_meia2 <= ingressos_restantes:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_meia2))
                                            lucro_meia2 = quantidade_meia2 * (valor_ingresso / 2)
                                            acumulucromeia2 += lucro_meia2
                                            print('Arrecadação de: R${}'.format(lucro_meia2))
                                            ingressos_comprados += quantidade_meia2
                                            contmeia2 += quantidade_meia2
                                            #comprovação meia entrada
                                            for p in range(1, quantidade_meia2 + 1):
                                                print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                                while k == True:
                                                    if opcao2.isdigit():
                                                        opcao2 = int(opcao2)
                                                        if opcao2 == 1:
                                                            estudante += 1  # opção estudante
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        elif opcao2 == 2:
                                                            idoso += 1  # opção idoso
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        elif opcao2 == 3:
                                                            outro += 1  # opção outro
                                                            print('comprovação cadastrada!\n')
                                                            k = False
                                                        else:
                                                            print('OPÇÃO INVÁLIDA!\nTente novamente...')
                                                            print('=-' * 20)
                                                            print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                                    else:
                                                        print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                        print('=-' * 20)
                                                        print('Selecione o tipo de comprovação para a {} meia entrada:'.format(p))  # comprovação para a meia entrada
                                                        opcao2 = input('[ 1 ] estudante\n[ 2 ] idoso\n[ 3 ] outro')
                                            # cadastrar idades
                                            for m in range(1, quantidade_meia2 + 1):
                                                idade_meia = input('Digite a idade do {}° comprador:'.format(m))
                                                if idade_meia.isdigit():
                                                    idade_meia = int(idade_meia)
                                                    soma_idade_meia += idade_meia
                                                    qtd_idade_meia += 1
                                            if quantidade_meia2 >= ingcomissao:
                                                resultado = quantidade_meia2 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_meia2 < ingcomissao:
                                                resto += quantidade_meia2
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))
                                    else:
                                        print('DÍGITO INVÁLIDO!\nTente novamente...')
                                        print('=-' * 20)


                                #GRUPO 2 DESCONTO:
                                elif vendedor_comissionado2 == 3:
                                    print('Esse ingresso custa R${}'.format(valor_desconto))
                                    quantidade_desconto2 = input('Quantidade de ingressos que serão vendidos:')
                                    if quantidade_desconto2.isdigit():
                                        quantidade_desconto2 = int(quantidade_desconto2)
                                        if quantidade_desconto2 <= ingressos_restantes:
                                            print('{} Ingresso(s) vendido(s)'.format(quantidade_desconto2))
                                            lucro_desconto2 = quantidade_desconto2 * valor_desconto
                                            acumulucrodesc2 += lucro_desconto2
                                            ingressos_comprados += quantidade_desconto2
                                            print('Arrecadação de: R${}'.format(lucro_desconto2))
                                            contdesc2 += quantidade_desconto2
                                            # cadastrar idades
                                            for d in range(1, quantidade_desconto2 + 1):
                                                idade_desconto = input('Digite a idade do {}° comprador:'.format(d))
                                                if idade_desconto.isdigit():
                                                    idade_desconto = int(idade_desconto)
                                                    soma_idade_desconto += idade_desconto
                                                    qtd_idade_desconto += 1
                                                else:
                                                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                    print('=-' * 20)
                                            if quantidade_desconto2 >= ingcomissao:
                                                resultado = quantidade_desconto2 // ingcomissao
                                                ingressos_comissionados += resultado
                                            elif quantidade_desconto2 < ingcomissao:
                                                resto += quantidade_desconto2
                                                if resto >= ingcomissao:
                                                    resultado = resto // ingcomissao
                                                    ingressos_comissionados += resultado
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(ingressos_restantes))


                                #GRUPO 2 CORTESIA:
                                elif vendedor_comissionado2 == 4 and cortesia == 1:
                                    print('Esse ingresso é gratuito'.format(valor_desconto))
                                    quantidade_cortesia2 = input('Quantidade de ingressos que serão entregues:')
                                    if quantidade_cortesia2.isdigit():
                                        quantidade_cortesia2 = int(quantidade_cortesia2)
                                        if quantidade_cortesia2 <= numero_cortesias - cortesias_restantes:
                                            print('{} Ingresso(s) entregue(s)'.format(quantidade_cortesia2))
                                            contcort2 += quantidade_cortesia2
                                            # cadastrar idades
                                            for c in range(1, quantidade_cortesia2 + 1):
                                                idade_cortesia = input('Digite a idade do {}° comprador:'.format(c))
                                                if idade_cortesia.isdigit():
                                                    idade_cortesia = int(idade_cortesia)
                                                    soma_idade_cortesia += idade_cortesia
                                                    qtd_idade_cortesia += 1
                                                    cortesias_restantes += 1
                                                else:
                                                    print('DÍGITO INVÁLIDO!\nTente novamente...')
                                                    print('=-' * 20)
                                        else:
                                            print('A quantidade solicitada é maior que os ingressos restantes\nRestam {} ingressos'.format(numero_cortesias - cortesias_restantes))
                    else:
                        print('DÍGITO INVÁLIDO!\nTente novamente...')
                        print('=-' * 20)
                else:
                    print('VENDEDOR NÃO CADASTRADO!')
                    print('=-' * 20)


            # RELATÓRIO:
            #inicio
            elif vendas == 3 or ingressos_restantes == 0 and numero_cortesias - cortesias_restantes == 0:
                print('=-' * 40)
                print(' ' * 20, 'RELATÓRIO:', ' ' * 20)
                print('=-' * 40)
                print('Quantidade ingressos emitidos: {}'.format(ingressos_comprados + ingressos_comissionados))
                print('Quantidade de ingressos não emitidos: {}\n\n'.format(ingressos_restantes))
                print('Inteiras: {}'.format(contint + contint1 + contint2))
                #ingressos cadastrados
                if meia_entrada == 1:
                    print('Meia-entradas: {}'.format(contmeia + contmeia1 + contmeia2))
                else:
                    print('MEIA ENTRADA NÃO CADASTRADA')
                if desconto == 1:
                    print('Descontos: {}'.format(contdesc + contdesc1 + contdesc2))
                else:
                    print('DESCONTO NÃO CADASTRADO')
                if cortesia == 1:
                    print('Cortesias: {}'.format(contcort + contcort1 + contcort2))
                else:
                    print('CORTESIA NÃO CADASTRADA')

                #dados meia entrada
                if meia_entrada == 1:
                    print('MEIA-ENTRADA:')
                    print('Quantidade de meia-entradas emitidas: {}'.format(contmeia + contmeia1 + contmeia2))
                    print('Meia-entradas para estudantes: {}'.format(estudante))
                    print('Meia-entradas para idosos: {}'.format(idoso))
                    print('Meia-entradas através de outros critérios: {}\n\n'.format(outro))
                #dados desconto
                if desconto == 1:
                    print('DESCONTO:\n')
                    print('Quantidade de ingressos emitidos com desconto: {}\n\n'.format(contmeia + contmeia1 + contmeia2))
                #dados cortesia
                if cortesia == 1:
                    print('CORTESIA:')
                    print('Quantidade total cortesias: {}'.format(numero_cortesias))
                    print('Cortesias emitidas: {}\n\n'.format(qtd_idade_cortesia))
                #dados vendedores comuns
                print('VENDEDORES COMUNS:')
                print('Total de ingressos vendidos: {}'.format(contint + contmeia + contdesc))
                print('''Ingressos inteiros: {}
Meia-entradas: {}
Descontos: {}'''.format(contint, contmeia, contdesc))
                print('Cortesias entregues: {}'.format(contcort))

                #dados comissionados
                if comissao == 1:
                    print('VENDEDORES COMISSIONADOS: {} e {}\n'.format(grupo1, grupo2))
                    print('Quantidade de cortesias para vendedores comissionados: {}\n'.format(ingressos_comissionados))
                    print('Ingressos vendidos por comissionados: {}\n'.format(contint1 + contint2 + contmeia1 + contmeia2 + contdesc1 + contdesc2))

                    # dados grupo de comissão 1
                    print('Ingressos vendidos pelo grupo {}: {}'.format(grupo1, (contint1 + contmeia1 + contmeia2)))
                    print('''Ingressos inteiros: {}
Meia-entradas: {}
Descontos: {}'''.format(contint1, contmeia1, contdesc1))
                    print('Cortesias entregues: {}\n'.format(contcort1))

                    # dados grupo de comissão 2
                    print('Ingressos vendidos pelo grupo {}: {}\n'.format(grupo2, (contint2 + contmeia2 + contmeia2)))
                    print('''Ingressos inteiros: {}
Meia-entradas: {}
Descontos: {}'''.format(contint2, contmeia2, contdesc2))
                    print('Cortesias entregues: {}\n'.format(contcort2))

                #arrecadação
                print('ARRECADAÇÃO:\n')
                print('Total arrecadado: R${}'.format(acumulucroint + acumulucroint1 + acumulucroint2 + acumulucromeia + acumulucromeia1 + acumulucromeia2 + acumulucrodesc + acumulucrodesc1 + acumulucrodesc2))
                print('Ingressos inteiros: R${}'.format(acumulucroint + acumulucroint1 + acumulucroint2))
                print('Meia-entradas: R${}'.format(acumulucromeia + acumulucromeia1 + acumulucromeia2))
                print('Descontos: R${}:'.format(acumulucrodesc + acumulucrodesc1 + acumulucrodesc2))

                totalint = contint + contint1 + contint2
                totalmeia = contmeia + contmeia1 + contmeia2
                totaldesc = contmeia + contmeia1 + contmeia2

                #tipo de ingresso mais vendido
                print('TIPO DE INGRESSO MAIS VENDIDO:')
                if totalint > totalmeia and totalint > totaldesc:
                    print('INTEIRA')
                elif totalmeia > totalint and totalmeia > totaldesc:
                    print('MEIA-ENTRADA')
                elif totaldesc > totalint and totaldesc > totalmeia:
                    print('DESCONTO')
                elif totalint == totalmeia and totalint > totaldesc and totalmeia > totaldesc:
                    print('INTEIRA E MEIA-ENTRADA')
                elif totalint == totaldesc and totalint > totalmeia and totaldesc > totalmeia:
                    print('INTEIRA E DESCONTO')
                elif totalmeia == totaldesc and totalmeia > totalint and totaldesc > totalint:
                    print('MEIA-ENTRADA E DESCONTO')
                else:
                    print('INTEIRA, MEIA-ENTRADA E DESCONTO')

                #média de idade
                if (soma_idade_int + soma_idade_meia + soma_idade_desconto) / (qtd_idade_int + qtd_idade_meia + qtd_idade_desconto + 1) >= 1:
                    print('MÉDIA DE IDADE DOS COMPRADORES:')
                    med = (soma_idade_int + soma_idade_meia + soma_idade_desconto) / (qtd_idade_int + qtd_idade_meia + qtd_idade_desconto)
                    print('Média: {:.1f}'.format(med))

                if soma_idade_cortesia / (qtd_idade_cortesia + 1) >= 1:
                    print('\nMÉDIA DE IDADE DAS CORTESIAS:')
                    print(soma_idade_cortesia / qtd_idade_cortesia)
                i = False
                j = False
        else:
            print('DÍGITO INVÁLIDO!\nTente novamente...')
            print('=-' * 20)