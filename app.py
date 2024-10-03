# dicionario
usuario = {
        "nome":"Joao",
        "idade":39,
        "profissao":"Programador",
        "email":"email@email.com"
    }

# adicionando nova chave
usuario["nome"] = input("Informe o nome: ")
usuario["idade"] = int(input("Informe a idade: "))
usuario["profissao"] = input("Informe a profissão: ")
usuario["email"] = input("Informe o e-mail: ")

# exibir os valores do dicionario na tela
print("DADOS DO USUARIO:\n")
print(f"Nome do usuário: {usuario.get("nome")}.")
print(f"Idade do usuário: {usuario["idade"]}.")
print(f"Profissão do usuário: {usuario["profissao"]}.")
print(f"E-mail do usuário: {usuario["email"]}.")