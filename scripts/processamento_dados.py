import json
import csv

class Dados:

   def __init__(self, dados, origem='memoria'):
      self.path = origem
      self.dados = dados
      self.nome_colunas = self.__get_columns()
      self.qtd_linhas = self.__size_data()
   
   @staticmethod
   def __leitura_json(path):
      with open(path, 'r') as file:
         return json.load(file)

   @staticmethod
   def __leitura_csv(path):
      dados_csv = []
      with open(path, 'r') as file:
         spamreader = csv.DictReader(file, delimiter=',')
         for row in spamreader:
            dados_csv.append(row)
      return dados_csv

   @classmethod
   def from_file(cls, path, tipo_dados):
      if tipo_dados.lower() == 'csv':
         dados = cls.__leitura_csv(path)
      elif tipo_dados.lower() == 'json':
         dados = cls.__leitura_json(path)
      else:
         raise ValueError('Tipo de dados inválido para leitura de arquivo.')
      return cls(dados, origem=path)
      
   @classmethod
   def from_memory(cls, dados):
      return cls(dados)
   
   def __get_columns(self):
      return list(self.dados[-1].keys())
   
   def __size_data(self):
      return len(self.dados)

   def rename_columns(self, key_mapping):
      new_dados = []

      for old_dict in self.dados:
         dict_temp = {}
         for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
         new_dados.append(dict_temp)
         
      self.dados = new_dados
      self.nome_colunas = self.__get_columns()

   @classmethod
   def join(cls, dadosA, dadosB):
      dados_combinados = dadosA.dados + dadosB.dados
      return cls.from_memory(dados_combinados)

   def __transformacao_dados_tabela(self):
      dados_combinados_tabela = [self.nome_colunas]

      for row in self.dados:
         linha = []
         for coluna in self.nome_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
         dados_combinados_tabela.append(linha)

      return dados_combinados_tabela

   def salvando_dados(self, path):

      dados_combinados_tabela = self.__transformacao_dados_tabela()

      with open(path, 'w') as file:
         writer = csv.writer(file)
         writer.writerows(dados_combinados_tabela)
