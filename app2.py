# tupla
import time


campos = ("Nome", "Idade", "Profissão", "E-mail")

# dicionario
usuario = {}

# entrada de dados
for campo in campos:
    usuario[campo] = input(f"Informe o valor do campo {campo}: ")

# exibir os valores do dicionario na tela
print("DADOS DO USUARIO:\n")
for campo in campos:
    print(f"{campo}: {usuario.get(campo)}.")
    time.sleep(1)