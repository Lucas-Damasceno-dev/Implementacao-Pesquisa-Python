# Variaveis
cont_menu = 0
tot_mulheres = 0


# Input's
while True:
    if cont_menu == 0:
        idade = int(input('Qual a sua idade? [10 à 100] '))
        cont_menu += 1

        sexo = int(input('1 - Masculino\n'
                         '2 - Feminino\n'
                         '3 - Voltar\n'
                         'Qual seu sexo?  '))
        if sexo == 1:
            cont_menu += 1
        if sexo == 2:
            tot_mulheres += 1
            cont_menu += 1
        if sexo == 3:
            cont_menu -= 1

        if cont_menu == 2:
            situacao = int(input('1 - Veterano\n'
                                 '2 - Egresso\n'
                                 '3 - Voltar\n'
                                 'Veterano ou Egresso?  '))
            if situacao == 1:
                cont_menu += 1
            if situacao == 3:
                cont_menu -= 1
            if situacao == 2:
                cont_menu += 1
                escolaridade = int(input('1 - Especialização\n'
                                         '2 - Graduação\n'
                                         '3 - Mestrado\n'
                                         '4 - Doutorado\n'
                                         '5 - Voltar\n'
                                         'Qual é seu grau de escolaridade?  '))
                if 0 < escolaridade < 5:
                    cont_menu += 1
                if escolaridade == 5:
                    cont_menu -= 1
            if cont_menu == 3:
                '''
            formatura = int(input('Que ano irá se formar? [ano_atual à 2060] '))
            formou = int(input('(PARA EGRESSOS)\n '
                               'Em que ano se formou? [1900 à ano_atual] '))
            pbl = int(input('0 - Não Concordo\n'
                            '1 - Concordo\n'
                            '2 - Não Tenho Opinião\n'
                            'Você concorda que o PBL ajuda na execução de seus trabalhos?  '))
            mercado = int(input('0 - Não Concordo\n'
                                '1 - Concordo\n'
                                '2 - Não Tenho Opinião\n'
                                'O mercado de trabalho local é capaz de reter os profissionais formados nas áreas de informática e '
                                'engenharia?'))
            novatos_pbl = int(input('0 - Não Concordo\n'
                                    '1 - Concordo\n'
                                    '2 - Não Tenho Opinião\n'
                                    'Você concorda que os alunos desconhecem o PBL quando entram no curso?'))
            adaptacao = int(input('0 - Não concordo\n'
                                  '1 - Concordo\n'
                                  '2 - Não Tenho Opinião\n'
                                  'Concorda com a afirmação de qua um aluno só consegue se adaptar com o PBL somente a partir do 4º'
                                  ' semestre?'))'''
# Processamento


# Saida
