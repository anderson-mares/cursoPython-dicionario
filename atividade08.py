# Crie um programa que faça o cadastro de vários usuários dentro de uma única lista. 
# Ao final, o programa deverá exibir na tela todos os dados de todos os usuários cadastrados. 
# Os dados do usuário a serem cadastrados serão os seguintes:
#
# - Nome
# - Idade
# - CPF
# - E-mail
# - Profissão
# - Tipo Sanguíneo
# - Peso
# - Altura
# 
# Ao terminar, envie para o GitHub e poste o link.

# tupla
atributos = ("Nome", "Idade", "CPF", "E-mail", "Profissão", "Tipo Sanguíneo", "Peso", "Altura")

# cadastrar um novo usuário
usuario = {}
for atributo in atributos:
    usuario[atributo] = input(f"Inform o valor do campo {atributo}: ")

# exibir os dados
print("")
for atributo in atributos:
    print(f"{atributo}: {usuario.get(atributo)}.")