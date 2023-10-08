def menu():
    while True:
        opcao = input('''
          ========================================
                    PROJETO AGENDA EM PYTHON
          MENU:
          [1]CADASTRAR CONTATO
          [2]LISTAR CONTATO
          [3]DELETAR CONTATO 
          [4]BUSCAR CONTATO PELO ID
          [5]BUSCAR CONTATO PELO NOME
          [6]SAIR
          ========================================
        ESCOLHA UMA OPÇÃO ACIMA: []
        ''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listaContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloId()
        elif opcao == "5":
            buscarContatoPeloNome()
        elif opcao == "6":
            sair()
            break
        else:
            print("Opção inválida")

def cadastrarContato():
    nome = input("Escreva o nome do contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o email do contato: ")
    try:
        with open("agenda.txt", "r") as agenda:
            linhas = agenda.readlines()
            if linhas:
                ultima_linha = linhas[-1].strip().split(';')
                ultimo_id = int(ultima_linha[0])
            else:
                ultimo_id = 0

        novo_id = ultimo_id + 1

        with open("agenda.txt", "a") as agenda:
            dados = f'{novo_id};{nome};{telefone};{email}\n'
            agenda.write(dados)
        print(f"Contato cadastrado com sucesso. ID: {novo_id}")
    except Exception as e:
        print(f"Erro ao cadastrar o contato: {e}")

def listaContato():
    try:
        agenda = open("agenda.txt", "r")
        for linha in agenda:
            idContato, nome, telefone, email = linha.strip().split(';')
            print(f"ID: {idContato}, Nome: {nome}, Telefone: {telefone}, Email: {email}")
        agenda.close()
    except Exception as e:
        print(f"Erro ao listar contatos: {e}")

def deletarContato():
    id_a_deletar = input("Digite o ID do contato que deseja deletar: ")
    try:
        with open("agenda.txt", "r") as agenda:
            linhas = agenda.readlines()
        with open("agenda.txt", "w") as agenda:
            for linha in linhas:
                idContato, _, _, _ = linha.strip().split(';')
                if idContato != id_a_deletar:
                    agenda.write(linha)
        print(f"Contato com ID {id_a_deletar} deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar contato: {e}")

def buscarContatoPeloId():
    id_a_buscar = input("Digite o ID do contato que deseja buscar: ")
    try:
        agenda = open("agenda.txt", "r")
        encontrado = False
        for linha in agenda:
            idContato, nome, telefone, email = linha.strip().split(';')
            if idContato == id_a_buscar:
                print(f"ID: {idContato}, Nome: {nome}, Telefone: {telefone}, Email: {email}")
                encontrado = True
                break
        if not encontrado:
            print(f"Contato com ID {id_a_buscar} não encontrado.")
        agenda.close()
    except Exception as e:
        print(f"Erro ao buscar contato pelo ID: {e}")

def buscarContatoPeloNome():
    nome_a_buscar = input("Digite o nome do contato que deseja buscar: ")
    try:
        agenda = open("agenda.txt", "r")
        encontrado = False
        for linha in agenda:
            idContato, nome, telefone, email = linha.strip().split(';')
            if nome.lower() == nome_a_buscar.lower():
                print(f"ID: {idContato}, Nome: {nome}, Telefone: {telefone}, Email: {email}")
                encontrado = True
        if not encontrado:
            print(f"Contato com nome '{nome_a_buscar}' não encontrado.")
        agenda.close()
    except Exception as e:
        print(f"Erro ao buscar contato pelo nome: {e}")

def sair():
    print("Encerrando o programa. Obrigado por usar a agenda em Python!")

def main():
    menu()

if __name__ == "__main__":
    main()
