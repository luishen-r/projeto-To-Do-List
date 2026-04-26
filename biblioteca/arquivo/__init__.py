def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as a:
            for linha in a:
                dado = linha.strip().split(';')
                print(f'{dado[0]:<20}{dado[1]:>3} ')
    except Exception as e:
        print(f'ERRO ao ler o arquivo! {e}')


def novoCadastro(nome, tarefa='<Desconhecido>', status='✘'):
    try:
        with open(nome, 'at', encoding='utf-8') as a:
            a.write(f'{tarefa};{status}\n')
        print(f'Nova tarefa "{tarefa}" adicionada com sucesso!')
    except Exception as e:
        print(f'ERRO ao escrever no arquivo! {e}')


def marcarConcluida(nome, tarefa):
    try:
        with open(nome, 'rt', encoding='utf-8') as a:
            linhas = a.readlines()
    except:
        print('ERRO ao ler o arquivo!')
        return

    alterado = False

    try:
        with open(nome, 'wt', encoding='utf-8') as a:
            for linha in linhas:
                dado = linha.strip().split(';')

                if dado[0] == tarefa:
                    dado[1] = '✔'
                    alterado = True

                a.write(f'{dado[0]};{dado[1]}\n')

        if alterado:
            print('Tarefa marcada como concluída!')
        else:
            print('Tarefa não encontrada.')

    except:
        print('ERRO ao escrever no arquivo!')


def removerTarefa(nome, tarefa):
    try:
        with open(nome, 'rt', encoding='utf-8') as arquivo:
            linhas = arquivo.readline()
    except:
        print('ERRO ao ler arquivos')
        return
    
    novas_linhas = []
    
    for linha in linhas:
        dado = linha.strip().split(';')  
        if dado[0] != tarefa:
            novas_linhas.append(linha)
    
    try:
        with open(nome, 'wt', encoding='utf-8') as arquivo:
            arquivo.writelines(novas_linhas)
    except:
        print('ERRO ao escrever no arquivo') 