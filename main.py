from usuarios.cadastro_usuario import realizar_cadastro_usuario, validar_credenciais
from produtos.listagem_produtos import menu_principal

while True:
    print("""BEM-VINDO 
            1- CADASTRAR
            2- LOGIN
            X- SAIR""")
    try:
        opcao = input ("DIGITE A OPÇÃO DESEJADA:") .upper()
        if opcao == "1":
            registro = realizar_cadastro_usuario()
            print("CADASTRO FEITO COM SUCESSO!")
        elif opcao == "2":
            autenticado = False
            while not autenticado:
                email_login = input("DIGITE SEU EMAIL: ").lower()
                senha_login = input("DIGITE SUA SENHA: ")
                autenticado = validar_credenciais(email_login, senha_login, registro)
                if autenticado :
                    menu_principal()
        elif opcao == "X":
            break
        else:
            print("OPÇÃO ESCOLHIDA É INVALIDA. ESCOLHA UMA OPÇÃO VÁLIDA!")
            continue
    except ValueError:
        print("SAINDO...")
        break
            