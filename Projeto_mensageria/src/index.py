from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, imprimirTitulo, limparTela

contatos = []

# FUNÇÕES
def AdicionarContato():
    imprimirTitulo("Criar Novo Contato")

    (nome, numero) = ObterDadosParaCadastroUsuario()

    novoContato = Contato(nome, numero)
    contatos.append(novoContato)

    print("Contato Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def ImprimirListaDeContatos():
    imprimirTitulo("Meus Contatos")

    if not any(contatos):
        print("Sua lista de contatos está vazia!")
    else:
        ListarContatos()

    print("")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    if not any(contatos):
        print("Você não possui nenhum contato para alterar")
        return

    ListarContatos()
    idxUsuario = int(input("Escolha um contato para alterar pelo número(#): ")) - 1

    (nome, numero) = ObterDadosParaCadastroUsuario(True)

    contatos[idxUsuario].nome = nome
    contatos[idxUsuario].numero = numero

    print("Contato Atualizado com Sucesso")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    destinatario = Contato("Contato para envio", "Numero para envio")
    mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    print("Mensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EnviarMensagem():
    # SUA LÓGICA AQUI
    print("Mensagem Enviada com Sucesso!")
    print("Faltam 0 mensagens na Fila!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def ObterDadosParaCadastroUsuario(paraEdicao = False):
    contatoValido = False
    mensagemNome = "Digite o nome do contato: " if not paraEdicao else "Digite o novo nome do contato: "
    mensagemNumero = "Digite o numero de telefone do contato: " if not paraEdicao else "Digite o novo numero de telefone do contato: "

    while not contatoValido:
        nome = input(mensagemNome)
        numero = input(mensagemNumero)

        contatoExiste = any(contato.nome == nome and contato.numero == numero for contato in contatos)

        if nome == "" and numero == "":
            print("\nNome ou Numero de Telefone estão inválidos! Favor digite novamente!\n")
        elif contatoExiste:
            print("\nContato Já Existe na Base! Favor incluir outro!\n")
        else:
            contatoValido = True

    return (nome, numero)

def ListarContatos():
    for i in range(0, len(contatos)):
        print(f"#{i + 1} - Nome: {contatos[i].nome}. Numero: {contatos[i].numero}")

# PROGRAMA PRINCIPAL
imprimirTitulo("SISTEMA DE MENSAGENS")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções:")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        ImprimirListaDeContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 5:
        EnviarMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")