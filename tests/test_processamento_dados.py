import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from processamento_dados import Dados

# from scripts.processamento_dados import Dados

@pytest.fixture
def dados_exemplo():
   dados = [
      {"nome": "Ana", "idade": 30},
      {"nome": "João", "idade": 25}
   ]
   return Dados.from_memory(dados)

def test_qtd_linhas(dados_exemplo):
   assert dados_exemplo.qtd_linhas == 2

def test_nome_colunas(dados_exemplo):
   assert set(dados_exemplo.nome_colunas) == {"nome", "idade"}

def test_join():
   dados_a = Dados.from_memory([{"a": 1}, {"a": 2}])
   dados_b = Dados.from_memory([{"a": 3}, {"a": 4}])
   combinados = Dados.join(dados_a, dados_b)
   assert combinados.qtd_linhas == 4
   assert combinados.dados[-1]["a"] == 4

def test_rename_columns(dados_exemplo):
   dados_exemplo.rename_columns({"nome": "primeiro_nome", "idade": "anos"})
   assert "primeiro_nome" in dados_exemplo.nome_colunas
   assert "nome" not in dados_exemplo.nome_colunas