lista_alunos = []
while True:
    opcoes = int(input('Menu do cadastro de alunos:\n' \
    '1. Adicionar aluno\n' \
    '2. Listar todos os alunos\n' \
    '3. Buscar aluno pelo nome\n' \
    '4. Remover aluno\n' \
    '5. Mostrar média geral das notas\n' \
    '6. Sair\n' \
    'Escolha uma das opções: '))

    def cadastro_alunos(opcoes): 
        match opcoes:
            case 1:
                dicionario_alunos = {
                    'nome':input('Digite o nome do aluno: '),
                    'idade':input('Digite a idade do aluno: '),
                    'nota':float(input('Digite a nota do aluno: '))
                    }
                lista_alunos.append(dicionario_alunos)
            case 2:
                print(f'Aqui esta a lista de alunos: {lista_alunos}')
            case 3:
                nome_busca = input('Digite o nome do aluno que deseja buscar: ')
                encontrado = False
                for aluno in lista_alunos:
                    if nome_busca == aluno['nome']:
                        print(f'Os dados do aluno são: {aluno}')
                        encontrado = True
                if not encontrado:
                       print('ALUNO NÃO ENCONTRADO')
            case 4:
                nome_busca2 = input('Digite o nome do aluno que deseja buscar: ')
                encontrado = False
                for aluno in lista_alunos:
                    if nome_busca2 == aluno['nome']:
                        lista_alunos.remove(aluno)
                        encontrado = True
                if not encontrado:
                        print('ALUNO NÃO ENCONTRADO')
            case 5:
                quantidade_aluno = len(lista_alunos)
                soma = 0
                for aluno in lista_alunos:
                    soma+=aluno['nota']
                if len(lista_alunos) == 0:
                    print('ALUNO INEXISTENTE')
                else:
                    media = soma / quantidade_aluno
                    print(f'A média dos alunos é: {media}')
    if opcoes == 6:
        print("Obrigado por tudo, fechando sistema...")
        print("Sistema fechado.")
        break

    cadastro_alunos(opcoes)