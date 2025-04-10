TarefaDic = {}
escolha: str = 'escolha'

def Cadastrar():
    while True:
        tarefa = str(input("\nDigite a sua tarefa (titulo): "))
        if tarefa != '':
            TarefaDic[tarefa] = 'Pendente'
            print(f"\nTarefa '{tarefa}' cadastrada com sucesso!\n")
            break
        else:
            print("\nTarefa não pode estar vazia\n")

def Listar():
    if TarefaDic:
        for i, (titulo, status) in enumerate(TarefaDic.items()):
            print(f"{i + 1}ª: Titulo = {titulo}, Status = {status}")
        return True
    print("\nSem tarefas cadastradas!\nTente adicionar uma tarefa!\n")
    return False

def Concluir():
    cheked = Listar()
    if not cheked:
        return
    
    while True:
        TarefaP = input(f"\nDigite qual tarefa você concluiu das acima:\n")
        if TarefaP in TarefaDic:
            TarefaDic[TarefaP] = 'Concluido'
            print("\nTarefa Concluida!\n")
            break
        else:
            print("\nTarefa não Existe, tente digitar algo valido\n")

def Excluir():
    cheked = Listar()
    if not cheked:
        return

    while True:
        TarefaE = input(f"\nDigite qual tarefa você vai excluir das acima:\n")
        if TarefaE in TarefaDic:
            TarefaDic.pop(TarefaE)
            print(f"\nTarefa '{TarefaE}' excluida com sucesso!\n")
            break
        else:
            print("\nTarefa não Existe, tente digitar algo valido\n")
    

print("Bem vindo")

while escolha != '':
    escolha = str(input("O que gostaria de fazer agora?\n"
                + "- Para Cadastrar tarefa digite '1'\n"
                + "- Para Listar tarefas digite '2'\n"
                + "- Para Concluir tarefa digite '3'\n"
                + "- Para Excluir tarefa digite '4'\n"
                + "- Caso queira parar digite deixe em branco\n"
                + "Digite sua escolha: "))
    match escolha:
        case '1':
            Cadastrar()
        case '2':
            Listar()
        case '3':
            Concluir()
        case '4':
            Excluir()
        case '':
            pass
        case _: 
            print("Digite algo valido, Tente novamente!")