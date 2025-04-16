import json
import csv

class Dados:


   def __init__(self, path, tipo_dados):
      self.path = path
      self.tipo_dados = tipo_dados
      self.dados = self.leitura_dados()
   
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
      if(self.tipo_dados.lower() == 'csv'):
         dados = self.leitura_csv()
         return dados
      elif (self.tipo_dados.lower() == 'json'):
         dados = self.leitura_json()
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

   def transformacao_dados_tabela(dados, nomes_colunas):
      dados_combinados_tabela = [nomes_colunas]

      for row in dados:
         linha = []
         for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
         dados_combinados_tabela.append(linha)

      return dados_combinados_tabela

   def salvando_dados(path, dados):
      with open(path, 'w') as file:
         writer = csv.writer(file)
         writer.writerows(dados)
