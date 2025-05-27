import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

dados_empresaB = Dados(path_csv, 'csv')
dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)

#transforme

key_mapping = {'Nome do Item': 'Nome do Produto',
           'Classificação do Produto':'Categoria do Produto',
           'Valor em Reais (R$)':'Preço do Produto (R$)',
           'Quantidade em Estoque':'Quantidade em Estoque',
           'Nome da Loja':'Filial',
           'Data da Venda': 'Data da Venda'}


dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)
print(dados_empresaB.size_data())


dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print(dados_fusao)
print(dados_fusao.qtd_linhas)

# load
path_dados_combined = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combined)
print(path_dados_combined)