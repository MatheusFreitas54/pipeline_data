import json
import csv

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

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
   dados = []
   if(tipo_arquivo.lower() == 'csv'):
      dados = leitura_csv(path)
      return dados
   elif (tipo_arquivo.lower() == 'json'):
      dados = leitura_json(path)
      return dados
   else:
      return print('Tipo de dados inválido!')
   
def get_columns(dados):
   return list(dados[0].keys())

def rename_columns(dados, key_mapping):
   new_dados = []

   for old_dict in dados:
      dict_temp = {}
      for old_key, value in old_dict.items():
         dict_temp[key_mapping[old_key]] = value
      new_dados.append(dict_temp)
      
   return new_dados

def size_data(dados):
   return len(dados)

def join(dadosA, dadosB):
   combined_list = []
   combined_list.extend(dadosA)
   combined_list.extend(dadosB)

   return combined_list

dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f"Nome colunas dados json: {nome_colunas_json}")
print(f"Dados json: {dados_json[0]}")
print(f"Quantidade de dados json: {tamanho_dados_json}")

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

#Transformação dos dados

dados_csv = leitura_dados(path_csv, 'csv')
dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)

print(f"Nome colunas dados csv: {nome_colunas_csv}")
print(f"Dados csv: {dados_csv[0]}")
print(f"Quantidade de dados csv: {tamanho_dados_csv}")


#União do dados:

dados_unidos = join(dados_json, dados_csv)
nome_colunas_unidas = get_columns(dados_unidos)
tamanho_dados_unidos = size_data(dados_unidos)

print(f"Nome das Colunas novas: {nome_colunas_unidas}")
print(f"Quantidade de dados unidos: {tamanho_dados_unidos}")