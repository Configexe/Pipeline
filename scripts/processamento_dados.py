import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados # Este é o atributo correto
        self.dados = self.leitura_dados() # Chama o método para carregar os dados
        self.nome_colunas = self.getcolumns()

    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json


    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    def leitura_dados(self):
        dados = []

        if self.tipo_dados == 'csv': 
            dados = self.leitura_csv()
        elif self.tipo_dados == 'json': 
            dados = self.leitura_json()
        return dados
        
    def getcolumns(self):
        return list(self.dados[-1].keys())
    
    
    def rename_columns(self, key_mapping):
        new_dados = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.dados = new_dados
        self.nome_colunas = self.getcolumns()