TarefaDic = {}
escolha: str = 'escolha'

def Cadastrar():
    tarefa = input("Digite a sua tarefa (titulo): ")
    TarefaDic[tarefa] = 'Pendente'
    
def Listar():
    for i, (titulo, status) in enumerate(TarefaDic.items()):
        print(f"{i + 1}°: Titulo = {titulo}, Status = {status}")

def Concluir():
    input
    Listar()

def Excluir():
    pass

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
            escolha = ''
        case _: 
            print("Digite algo valido, Tente novamente!")