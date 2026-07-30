def arquivoExiste(nome):
    try:
        with open(nome, 'rt') as a:
            ...
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        with open(nome, 'wt+', encoding='utf8'):
            ...
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as a:
            for linha in a:
                dado = linha.strip().split(';')
                if len(dado) == 2:
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
    except Exception as e:
        print(f'ERRO ao ler o arquivo! {e}')
        return

    novas_linhas = []
    alterado = False

    for linha in linhas:
        dado = linha.strip().split(';')
        if len(dado) == 2:
            if dado[0] == tarefa:
                dado[1] = '✔'
                alterado = True
            novas_linhas.append(f'{dado[0]};{dado[1]}\n')
        else:
            novas_linhas.append(linha)  # Mantém linhas fora do padrão sem quebrar

    if alterado:
        try:
            with open(nome, 'wt', encoding='utf-8') as a:
                a.writelines(novas_linhas)
            print('Tarefa marcada como concluída!')
        except Exception as e:
            print(f'ERRO ao escrever no arquivo! {e}')
    else:
        print('Tarefa não encontrada.')


def removerTarefa(nome, tarefa):
    try:
        with open(nome, 'rt', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except Exception as e:
        print(f'ERRO ao ler o arquivo! {e}')
        return
    
    novas_linhas = []
    removido = False

    for linha in linhas:
        dado = linha.strip().split(';')  
        if dado[0] != tarefa:
            novas_linhas.append(linha)
        else:
            removido = True
    
    if removido:
        try:
            with open(nome, 'wt', encoding='utf-8') as arquivo:
                arquivo.writelines(novas_linhas)
            print(f'Tarefa "{tarefa}" removida com sucesso!')
        except Exception as e:
            print(f'ERRO ao escrever no arquivo! {e}')
    else:
        print('Tarefa não encontrada para remoção.')
    

def editarTarefa(nome_arquivo, tarefa_antiga, nova_tarefa):
    try:
        with open(nome_arquivo, 'rt', encoding='utf-8') as a:
            linhas = a.readlines()
    except Exception as e:
        print(f'ERRO ao ler o arquivo! {e}')
        return

    novas_linhas = []
    alterado = False

    for linha in linhas:
        dado = linha.strip().split(';')
        if len(dado) == 2:
            # Se encontrou a tarefa que deseja alterar
            if dado[0] == tarefa_antiga:
                novas_linhas.append(f'{nova_tarefa};{dado[1]}\n')  # Atualiza o nome, mantém o status
                alterado = True
            else:
                novas_linhas.append(linha)
        else:
            novas_linhas.append(linha)  # Mantém linhas fora do padrão intactas

    if alterado:
        try:
            with open(nome_arquivo, 'wt', encoding='utf-8') as a:
                a.writelines(novas_linhas)
            print(f'Tarefa "{tarefa_antiga}" alterada para "{nova_tarefa}" com sucesso!')
        except Exception as e:
            print(f'ERRO ao escrever no arquivo! {e}')
    else:
        print(f'Tarefa "{tarefa_antiga}" não foi encontrada.')