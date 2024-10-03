import time

# tupla
atributos = ("Nome", "E-mail", "Profissão")

# lista de dicionarios
usuarios = [
    {
        atributos[0]:"Fulano",
        atributos[1]:"fulano@email.com",
        atributos[2]:"programador"
    },
    {
        atributos[0]:"Ciclano",
        atributos[1]:"ciclano@email.com",
        atributos[2]:"administrador"
    },
    {
        atributos[0]:"Beltrano",
        atributos[1]:"beltrano@email.com",
        atributos[2]:"recepcionista"
    }
]

# cadastrar um novo usuário
usuario = {}
for atributo in atributos:
    usuario[atributo] = input(f"Inform o valor do campo {atributo}: ")
usuarios.append(usuario)

# exibir os dados
for usuario in usuarios:
    print("")
    for atributo in atributos:
        print(f"{atributo}: {usuario.get(atributo)}.")