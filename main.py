from biblioteca.iniciador import *
from biblioteca.arquivo import *
from time import sleep

arquivo = 'tarefas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    menu('TO DO LIST')
    print('1- Adicionar Tarefas')
    print('2- Listar Tarefas')
    print('3- Marcar Tarefa como Concluída')
    print('4- Remover Tarefa')
    print('5- Sair')
    opc = leiaInt('Escolha sua opção: ')
    restrição(opc)
    sleep(2)
    
    if opc == 1:
        menu('ADICIONAR TAREFAS')
        tarefa = str(input('Informe qual tarefa deseja adicionar: ')).strip()
        novoCadastro(arquivo, tarefa)
    elif opc == 2:
        menu('LISTAR TAREFAS')
        lerArquivo(arquivo)
    elif opc == 3:
        menu('MARCAR COMO CONCLUIDA')
        tarefa = str(input('Informe a tarefa: ')).strip()
        marcarConcluida(arquivo, tarefa)
    elif opc == 4:
        menu('REMOVER TAREFA')
        tarefa = str(input('Informe que tarefa desja remover: ')).strip()
        removerTarefa(arquivo, tarefa)
    elif opc == 5:
        print('Encerrando TO DO LIST...')
        sleep(2)
        break