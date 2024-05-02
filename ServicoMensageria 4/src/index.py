from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela
from queue import Queue

# FUNÇÕES
lista_contatos = []
fila_contatos = Queue()

def AdicionarContato():
    # ESCREVER LÓGICA AQUI!
    # Exemplo de criação de um contato

    novo_nome = input("Digite o nome:  ")
    novo_telefone = input("Digite o telefone: ")
    for contato in lista_contatos:
        if contato == novo_telefone:
            print("\n Este telefone ja existe \n")
            return

    lista_contatos.append(novo_nome)
    lista_contatos.append(novo_telefone)

    print("\nUsuário Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def MostrarContatos():
    # ESCREVER LÓGICA AQUI

    print("Mostrando lista de contatos")
    print(lista_contatos)
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def EditarContato():

    print("Contato editado com sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def EscreverMensagem():
    nome_destinatario = input("Digite o nome do contato: ").upper()
    telefone_destinatario = input("Digite o telefone do contato: ")

    for contato in lista_contatos:
        if contato == telefone_destinatario:
            mensagem = input(
                f"Digite sua mensagem para {nome_destinatario}: ")
            data_mensagem = input(
                "Digite a data atual: ")
            fila_contatos.put(
                mensagem)
            print("\nMensagem Criada com Sucesso!")
            print(
                f"Existe(m) {fila_contatos.qsize()} mensagem(ns) na fila!")
            enviar_mensagem = input(
                "\n1- Deseja enviar a primeira mensagem?\n2- Deseja apagar a primeira mensagem?\n3- Voltar para o menu\n: ").strip().upper()
            if enviar_mensagem == "1":
                print("\nMensagem Enviada com Sucesso!")
                fila_contatos.get(mensagem)
                print(
                    f"Agora existe(m) {fila_contatos.qsize()} mensagem(ns) na fila!")
                print(
                    f"A mensagem {mensagem} foi enviada para {nome_destinatario} na data {data_mensagem}")
                input("[APERTE ENTER PARA CONTINUAR]")
                limparTela()
                return
            elif enviar_mensagem == "2":
                ApagarMensagem()
                return
            elif enviar_mensagem == "3":
                limparTela()
                return
            else:
                print("Opção Invalida!")
                input("\n[APERTE ENTER PARA CONTINUAR]")
                limparTela()
                return
    print("\nEste contato não está na sua lista!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def ApagarMensagem():
    if fila_contatos.empty():
        print("Não existem mensagens criadas no momento!")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()
        return
    else:
        print(
            f"\nAgora existe(m) {fila_contatos.qsize()} mensagem(ns) na fila!")
        apagar_mensagem = input(
            "\nDeseja apagar a primeira mensagem?   S/N      : ").strip().upper()
        if apagar_mensagem == "S":
            print("\nMensagem apagada com Sucesso!")
            fila_contatos.get()
            print(
                f"\nAgora existe(m) {fila_contatos.qsize()} mensagem(ns) na fila!")
            input("[APERTE ENTER PARA CONTINUAR]")
            limparTela()
            return
    limparTela()
    return


# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("\nEscolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        MostrarContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 5:
        ApagarMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("\nOpção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")
