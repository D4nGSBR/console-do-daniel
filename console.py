opcoes = int(input('OPÇÕES DO CONSOLE:\n' \
'1 - Calculadora\n' \
'2 - Cofre\n' \
'3 - Quiz\n' \
'4 - Sobre\n' \
'5 - Sair\n' \
'QUAL OPÇÃO DESEJA?: '))
match opcoes:
    case 1:
        num1 = float(input("ESCOLHA UM NUMERO: "))
        num2 = float(input("ESCOLHA OUTRO NUMERO: "))
        operacao = input("ESCOLHA UMA OPERAÇÃO: +, *, -, /: ")
        if operacao == '+':
            print(f" o resultado é {num1 + num2}")
        elif operacao == '-':
            print(f" o resultado é {num1 - num2}")
        elif operacao == '*':
            print(f" o resultado é {num1 * num2}")
        elif operacao == '/':
            print(f" o resultado é {num1 / num2}")
    case 2:
        nick_save = input('Crie um nome para sua conta: ')
        senha_save = input('Crie uma senha para sua conta!: ')
        coisas_cont = input('guarde suas informações (nós a guardaremos bem!!): ')
        nick_log = input('Digite o nome da sua conta: ')
        senha_log = input('Digite a senha da sua conta: ')
        if senha_log != senha_save and nick_save == nick_log:
          print('senha incorreta, tente novamente')
        if senha_log == senha_save and nick_save != nick_log:
          print('nome incorreto, tente novamente')
        if senha_log != senha_save and nick_save != nick_log:
          print('dados incorretos, tente novamente')
        if senha_log == senha_save and nick_log == nick_save:
          print(f'aqui estão seus dados: {coisas_cont}')
    case 3:
        pontos = 0

        res1 = input("1. Qual é a capital do Brasil? ").lower()
        if res1.lower() == "brasília":
            print("Correto!")
            pontos += 1
        else:
            print("Errado. A resposta é Brasília.")
        res2 = input("2. Qual é a maior floresta tropical do país? ").lower()
        if res2.lower() == "amazônia":
            print("Certo!")
            pontos += 1
        else:
            print("Incorreto. É a Amazônia.")
        res3 = input("3. Qual o nome da moeda oficial? ").lower()
        if res3.lower() == "real":
            print("Isso mesmo!")
            pontos += 1
        else:
            print("Errou. É o Real.")
        res4 = input("4. Qual o maior estado em tamanho? ").lower()
        if res4.lower() == "amazonas":
            print("Boa!")
            pontos += 1
        else:
            print("Errado, é o Amazonas.")
        res5 = input("5. Qual a religião com mais pessoas do Brasil? ").lower()
        if res5.lower() == "católica":
            print("Exato!")
            pontos += 1
        else:
            print("Resposta errada, correta: católica.")
        res6 = int(input("6. Em que ano o Brasil foi descoberto? "))
        if res6 == 1500:
            print("Acertou em cheio!")
            pontos += 1
        else:
            print("Errou. Foi em 1500.")
        res7 = int(input("7. Quantos estados o Brasil possui (sem contar o distrito federal)? "))
        if res7 == 26:
            print("Correto!")
            pontos += 1
        else:
            print("Errado. São 26 estados.")                  
        res8 = int(input("8. Em que ano o Brasil foi considerado independente? "))
        if res8 == 1822:
            print("Certo!")
            pontos += 1
        else:
            print("Errado. Foi em 1822.")
        res9 = int(input("9. Quantas vezes a seleção brasileira de futebol foi campeã mundial? "))
        if res9 == 5:
            print("Isso! Somos Hexa!")
            pontos += 1
        else:
            print("Errou. São 5 vezes.")
        res10 = input("10. Qual o nome da pessoa que descobriu o Brasil?? ")
        if res10.lower() == "pedro alvares cabral":
            print("Correto!")
            pontos += 1
        else:
            print("errou. foi Pedro Alvares cabral")
        print(f"\nFim do Quiz! Você marcou {pontos} de 10 pontos.")
    case 4:
        print('Criador: Daniel Gimenes Siqueira\n' \
        'Completo: 30/06/2026\n' \
        'Inicializado: 25/06/2026\n' \
        'Versão: 1.0\n' \
        'Obrigado por participar!!!')
    case 5:
        print('Obrigado por tudo!!! Tchau, até mais!!!')
    case _:
        print('POR FAVOR, ESCOLHA UMA DAS OPÇÕES')