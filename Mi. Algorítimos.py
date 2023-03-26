# Variaveis
cont_menu = 0
tot_mulheres = 0
tot_mulheres_egre = 0
cont_conc_perg5 = 0
nao_op_conc_perg6 = 0
ida_nao_per7 = []
ida_vao_formar = []
tot_conc_perg8 = 0
tot_alu_conc_nao_op_perg9 = 0
med_ida_vao_formar = 0
med_ida_nao_perg7 = 0

# Input's
while True:
    if cont_menu == 0:
        idade = int(input('Qual a sua idade? [10 à 100] '))
        if idade > 100 or idade < 10:
            print('Erro! Resposta inválida...')
        else:
            cont_menu += 1


    if cont_menu == 1:
        sexo = int(input('1 - Masculino\n'
                         '2 - Feminino\n'
                         '3 - Voltar\n'
                         'Qual seu sexo?  '))
        if sexo == 1:
            cont_menu += 1
        elif sexo == 2:
            tot_mulheres += 1
            cont_menu += 1
        elif sexo == 3:
            cont_menu -= 1
        else:
            print('Erro! Resposta inválida...')    


    if cont_menu == 2:
        situacao = int(input('1 - Veterano\n'
                             '2 - Egresso\n'
                             '3 - Voltar\n'
                             'Veterano ou Egresso?  '))
        if situacao > 3 or situacao < 1:
            print('Erro! Resposta inválida...')
        elif situacao == 1:
            formatura = int(input('Que ano irá se formar? [ano_atual à 2060] '))
            if formatura < 2023 or formatura > 2060:    
                print('Erro! Resposta inválida...')
            cont_menu += 1
            ida_vao_formar.append(idade)
            med_ida_vao_formar = sum(ida_vao_formar) / len(ida_vao_formar)
        elif situacao == 3:
            cont_menu -= 1
        else:
            if sexo == 2:
                tot_mulheres_egre += 1
                cont_menu += 1
            escolaridade = int(input('1 - Especialização\n'
                                     '2 - Graduação\n'
                                     '3 - Mestrado\n'
                                     '4 - Doutorado\n'
                                     '5 - Voltar\n'
                                     'Qual é seu grau de escolaridade?  '))
            if escolaridade > 5 or escolaridade < 1:
                print('Erro! Resposta inválida...')
            elif escolaridade == 5:
                cont_menu -= 1 
            else:
                formou = int(input('(PARA EGRESSOS)\n '
                                'Em que ano se formou? [1900 à ano_atual] '))
                if formou > 2023 or formou < 1900:
                    print('Erro! Resposta inválida...')
                else:
                    cont_menu += 1


    if cont_menu == 4:
        pbl = int(input('0 - Não Concordo\n'
                        '1 - Concordo\n'
                        '2 - Não Tenho Opinião\n'
                        'Você concorda que o PBL ajuda na execução de seus trabalhos?  '))
        if pbl > 2 or pbl < 0:
            print('Erro! Resposta inválida...')
        elif pbl == 1: 
            cont_menu += 1
            cont_conc_perg5 += 1
        else: 
            cont_menu += 1

        
    if cont_menu == 5:
        metodo = int(input('0 - Não Concordo\n'
                           '1 - Concordo\n'
                           '2 - Não Tenho Opinião\n'
                           'Você concorda que o PBL é melhor que o método tradicional de ensino?'))
        if metodo > 2 or metodo < 0:
            print('Erro! Resposta inválida...')
        elif metodo == 0 or metodo == 2:
            cont_menu += 1 
            nao_op_conc_perg6 += 1
        else:
            cont_menu += 1


    if cont_menu == 6: 
        mercado = int(input('0 - Não Concordo\n'
                            '1 - Concordo\n'
                            '2 - Não Tenho Opinião\n'
                            'O mercado de trabalho local é capaz de reter os profissionais formados nas áreas de informática e '
                            'engenharia?'))
        if mercado > 2 or mercado < 0:
            print('Erro! Resposta inválida...')
        elif mercado == 0:
            ida_nao_per7.append(idade)
            med_ida_nao_perg7 = sum(ida_nao_per7) / len(ida_nao_per7)
            cont_menu += 1
        else:
            cont_menu += 1


    if cont_menu == 7:
        novatos_pbl = int(input('0 - Não Concordo\n'
                                '1 - Concordo\n'
                                '2 - Não Tenho Opinião\n'
                                'Você concorda que os alunos desconhecem o PBL quando entram no curso?'))
        if novatos_pbl > 2 or novatos_pbl < 0:
            print('Erro! Resposta inválida...')
        elif novatos_pbl == 1:
            tot_conc_perg8 +=1
            cont_menu += 1
        else:
            cont_menu += 1


    if cont_menu == 8:   
        adaptacao = int(input('0 - Não concordo\n'
                              '1 - Concordo\n'
                              '2 - Não Tenho Opinião\n'
                              'Concorda com a afirmação de qua um aluno só consegue se adaptar com o PBL somente a partir do 4º'
                              ' semestre?'))
        if adaptacao > 2 or adaptacao < 0:
            print('Erro! Resposta inválida...')
        elif adaptacao == 1 or adaptacao == 0:
            tot_alu_conc_nao_op_perg9 += 1
            cont_menu += 1
        else:
            cont_menu += 1

    if cont_menu == 9:
        escolha = int(input('OBRIGADO PELA SUA OPINIÃO\n'
                            '\n'
                            'NOVO CADASTRO_________(01)\n'
                            'EXIBIR RELATORIO______(02)\n'
                            'VOLTAR PARA O MENU____(03)\n'
                            'OQUE DESEJA?  '))
        if escolha == 1:
            cont_menu = 0
        elif escolha == 2:
            break
        elif escolha == 3:
            cont_menu -= 1
        else:
            print('Erro! Resposta inválida...')



# Saida
print("\n")

print("\nRESULTADOS DA PESQUISA\n")

print(f"Total de mulheres que participaram: {tot_mulheres}")

print(f"Total de mulheres egressas que participaram: {tot_mulheres_egre}")

print(f"Total de pessoas que concordam que o PBL ajuda na execução de seus trabalhos: {cont_conc_perg5}")

print(f"Total de pessoas que não concordam ou não têm opinião sobre o PBL ser melhor que o método tradicional de ensino: {nao_op_conc_perg6}")

print(f"Média de idade das pessoas que não concordam que o mercado de trabalho local é capaz de reter os profissionais formados nas áreas de informática e engenharia: {med_ida_nao_perg7}")

print(f"Total de pessoas que concordam que o mercado de trabalho local é capaz de reter os profissionais formados nas áreas de informática e engenharia: {tot_conc_perg8}")

print(f"Total de alunos que concordam que não conheciam o PBL quando entraram no curso: {tot_alu_conc_nao_op_perg9}")

print(f"Média de idade das pessoas que concordam que irão se formar no futuro: {med_ida_vao_formar}")
