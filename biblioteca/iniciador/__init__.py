def menu(txt, tam=30):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def restrição(msg):
    if msg not in range(1, 6):
        print('ERRO Digite uma opção dentre as disponíveis')
        return False
    else:
        return True
            