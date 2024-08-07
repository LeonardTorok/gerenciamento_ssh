import os
import subprocess

def listar_usuarios():
    # Lista os usuários com acesso SSH
    try:
        with open('/etc/ssh/sshd_config', 'r') as file:
            print("Usuários com acesso SSH:")
            for line in file:
                if line.startswith("AllowUsers"):
                    usuarios = line.strip().split()[1:]  # Ignora a primeira palavra
                    print(", ".join(usuarios))
    except FileNotFoundError:
        print("Arquivo sshd_config não encontrado.")

def adicionar_usuario(username):
    # Adiciona um novo usuário
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        print(f"Usuário '{username}' adicionado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao adicionar usuário '{username}'.")

def remover_usuario(username):
    # Remove um usuário
    try:
        subprocess.run(['sudo', 'userdel', username], check=True)
        print(f"Usuário '{username}' removido com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao remover usuário '{username}'.")

def menu():
    while True:
        print("\nGerenciamento de Usuários SSH")
        print("1. Listar Usuários")
        print("2. Adicionar Usuário")
        print("3. Remover Usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            username = input("Digite o nome do usuário a ser adicionado: ")
            adicionar_usuario(username)
        elif opcao == '3':
            username = input("Digite o nome do usuário a ser removido: ")
            remover_usuario(username)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    menu()