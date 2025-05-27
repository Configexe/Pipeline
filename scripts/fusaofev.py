import json
import csv

from processamento_dados import Dados
#path


#funções da pipeline






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
#iniciando a leitura dos dados
#dados_csv = leitura_dados(path_csv,'csv')
#nome_colunas_csv = getcolumns(dados_csv)
#print(nome_colunas_csv)

#dados_json = leitura_dados(path_json,'json')
#nome_colunas_json = getcolumns(dados_json)
#print(nome_colunas_json)

#key_mapping = {'Nome do Item': 'Nome do Produto',
#           'Classificação do Produto':'Categoria do Produto',
#           'Valor em Reais (R$)':'Preço do Produto (R$)',
#           'Quantidade em Estoque':'Quantidade em Estoque',
#           'Nome da Loja':'Filial',
#           'Data da Venda': 'Data da Venda'}


#transformando os dados em uma coisa só
#dados_csv = rename_columns(dados_csv,key_mapping)
#nome_colunas_csv = getcolumns(dados_csv)
#print(nome_colunas_csv)


#dados_fusao = join(dados_json, dados_csv)
#nome_colunas_fusao = getcolumns(dados_fusao)
#tamanho_dados_fusao =size_data(dados_fusao)
#print(nome_colunas_fusao)
#print(tamanho_dados_fusao)


#salvando dados

#dados_fusao_tabela = transformando_dados_tabela(dados_fusao,nome_colunas_fusao)

#path_dados_combined = 'data_processed/dados_combinados.csv'

##salvando_dados(dados_fusao_tabela,path_dados_combined)

##print(path_dados_combined)