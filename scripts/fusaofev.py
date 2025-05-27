import json
import csv

from processamento_dados import Dados
#path
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#funções da pipeline

def salvando_dados(dados,path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def transformando_dados_tabela(dados, nomes_colunas):
    
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    
    return dados_combinados_tabela

def rename_columns(dados, key_mapping):
    new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados]
    return new_dados_csv

def getcolumns(dados):
    return list(dados[-1].keys())

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json


def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
            
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados=[]
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo =='json':
        dados = leitura_json(path)
    return dados

def size_data(dados):
    return len(dados)

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.dados)

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