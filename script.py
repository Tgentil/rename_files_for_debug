""" Script for rename files"""
import os

pasta = os.path.join(os.getcwd(), 'data')  # Caminho para a pasta "data" no diretório do script
CONTADOR = 1

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".pdf"):
        novo_nome = f"{CONTADOR} - documento ({CONTADOR})"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome + ".pdf")
        os.rename(caminho_antigo, caminho_novo)
        CONTADOR += 1
