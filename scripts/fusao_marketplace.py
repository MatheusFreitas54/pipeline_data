import json
import csv
from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.dados)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.dados)


# dados_json = leitura_dados(path_json, 'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)

# print(f"Nome colunas dados json: {nome_colunas_json}")
# print(f"Dados json: {dados_json[0]}")
# print(f"Quantidade de dados json: {tamanho_dados_json}")



# #Transformação dos dados

# dados_csv = leitura_dados(path_csv, 'csv')
# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)

# print(f"Nome colunas dados csv: {nome_colunas_csv}")
# print(f"Dados csv: {dados_csv[0]}")
# print(f"Quantidade de dados csv: {tamanho_dados_csv}")

# #União do dados:

# dados_unidos = join(dados_json, dados_csv)
# nome_colunas_unidas = get_columns(dados_unidos)
# tamanho_dados_unidos = size_data(dados_unidos)

# print(f"Nome das Colunas novas: {nome_colunas_unidas}")
# print(f"Quantidade de dados unidos: {tamanho_dados_unidos}")

# #Salvando dados

# dados_uniao_tabela = transformacao_dados_tabela(dados_unidos, nome_colunas_unidas)

# salvando_dados(path_dados_combinados, dados_uniao_tabela)
# print(path_dados_combinados)