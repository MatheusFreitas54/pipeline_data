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

#Extract

dados_empresaA = Dados.from_file(path_json, 'json')
dados_empresaB = Dados.from_file(path_csv, 'csv')

#Transform

dados_empresaB.rename_columns(key_mapping)
# print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
# print(dados_fusao)
# print(dados_fusao.qtd_linhas)

#Load

dados_fusao.salvando_dados(path_dados_combinados)
print(f"Dados criados e salvado em: {path_dados_combinados}")