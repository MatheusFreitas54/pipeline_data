# 📊 pipeline_data

Projeto em Python com foco em manipulação de dados utilizando orientação a objetos. O objetivo é criar uma estrutura reutilizável para carregar, transformar, combinar e exportar dados de forma simples e organizada.

## 📁 Estrutura do Projeto

```
.
├── .gitignore
├── README.md
├── data_processed
    └── .gitkeep
├── data_raw
    ├── dados_empresaA.json
    └── dados_empresaB.csv
├── notebooks
    ├── .gitkeep
    └── exploracao.ipynb
└── scripts
    ├── .gitkeep
    ├── fusao_marketplace.py
    └── processamento_dados.py
└── tests
    ├── test_processamento_dados.py

```

---

## 🚀 Funcionalidades

- 📥 Leitura de arquivos `CSV` e `JSON`
- 🧠 Representação dos dados como objetos da classe `Dados`
- 🔄 Junção de dois conjuntos de dados com `join()`
- ✏️ Renomear colunas de forma flexível
- 💾 Exportar os dados combinados para um novo arquivo `CSV`

---

## 🛠️ Instalação e Execução

1. **Clone o repositório**
   ```bash
   git clone https://github.com/MatheusFreitas54/pipeline_data.git
   cd pipeline_data
   ```
   
2. **(Opcional) Crie um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install requests==2.28.2
   pip install pandas==2.0.0
   pip install notebook==7.0.3
   pip install pytest
   ```
   `ou`

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o exemplo**

   python scripts/fusao_marketplace.py


---

## 🧠 Conceitos Utilizados

   - Orientação a Objetos com encapsulamento dos dados e comportamentos
   - Métodos Estáticos e de Classe **(@staticmethod, @classmethod)**
   - Boas práticas de reutilização de código
   - Trabalho com dados em memória e não apenas via arquivos

---

## 🔧 Melhorias Futuras

   - Adicionar suporte à leitura e escrita de arquivos Excel **(.xlsx)**
   - Implementar filtros personalizados e transformações por coluna
   - Interface CLI para manipulação sem código
   - Testes automatizados com **pytest ou unittest**

---

## Autor

Desenvolvido por Matheus Freitas ™