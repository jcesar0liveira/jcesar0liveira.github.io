def realizar_cadastro_usuario():
    registro_usuario = {}
    nome = input("Digite seu nome: ") .upper() .strip()
    telefone = str(input("INSIRA SEU TELEFONE: "))
    email = input("insira se email: ") .lower() .strip()
    senha = ""
    while True:
        senha = input("insira a senha:")
        if len(senha) < 5:
            print("a senha precisa ter no minimo 5 caracteres!")
            continue
        else:
            break
    
    registro_usuario["nome"] = nome
    registro_usuario["telefone"] = telefone
    registro_usuario[email] = senha
    return registro_usuario

def validar_credenciais(email, senha, registro):
    if email in registro:
        if registro[email] == senha:
            print("login bem-sucedido!")
            return True
        else:
            print("senha incorreta.")
            return False
    else:
            print("email não encontrado")
            return False
