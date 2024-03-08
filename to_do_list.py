# LISTA DE TAREFAS
""" status = Aberta/Concluida
    urgencia = SIM/NÃO
"""
from datetime import timedelta, date
import sys
ID = 0
tarefas = []


def adicionar_tarefa():
    """ ADICIONAR TAREFA"""
    id = ID+1
    nome = input('Digite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    status = 'Aberta'
    dataAtual = date.today()
    dataInicial = dataAtual.strftime("%d/%m/%Y")
    prazoInput = input('Digite o p>razo da tarefa em dias: ')
    prazoDias = int(prazoInput) if prazoInput.isdigit() else sys.exit(
        'Tipo de dado incorreto, a aplicação será finalizada!')
    dataFinal = (dataAtual + timedelta(days=prazoDias)).strftime("%d/%m/%Y")
    urgencia = "SIM" if input('Informe se a tarefa é urgente?\n' +
                              '(S)= SIM / (N)= NÃO\n') == "S" else "NÃO"
    tarefa = {"id": id, "nome": nome, "descricao": descricao, "status": status,
              "dataInicial": dataInicial, "dataFinal": dataFinal, "urgencia": urgencia}
    tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')


def listar_tarefas():
    """ LISTAR TAREFAS"""
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        for i, item in enumerate(tarefas, 1):
            print(f"{i}. Nome:{item['nome']} - Descricao:{item['descricao']} - Status:{item['status']} - Data de Criacao:{
                  item['dataInicial']} - Data de Conclusão:{item['dataFinal']} - Urgência:{item['urgencia']}")


def excluir_Tarefa():
    """ ADICIONAR TAREFA"""
    listar_tarefas()
    if not tarefas:
        return
    indice = int(input("Digite o número da tarefa que deseja exluir: \n")) - 1
    if 0 <= indice < len(tarefas):
        del tarefas[indice]
        print('Tarefa excluída com sucesso!')
    else:
        print("Índice inválido.")


def status_da_tarefa():
    """ MARCAR TAREFA COMO CONCLUÍDA"""
    listar_tarefas()
    if not tarefas:
        return
    indice = int(
        input("\nDigite o número da tarefa que deseja alterar: \n")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]['status'] = "Concluido"
        print('Status da Tarefa alterado com sucesso!')
    else:
        print("Índice inválido.")


# Menu com funções
while True:
    print("\n--- LISTA DE TAREFAS ---")
    print("1. Adicionar Tarefa")
    print("2. Excluir Tarefa")
    print("3. Listar Tarefas")
    print("4. Alterar Status da Tarefa")
    print("5. Sair\n")
    opcao = input("Ecolha uma opção:\n")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        if not tarefas:
            print('A lista está vazia')
        else:
            excluir_Tarefa()
    elif opcao == "3":
        if not tarefas:
            print('A lista está vazia')
        else:
            listar_tarefas()
    elif opcao == "4":
        status_da_tarefa()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente Novamente.")
