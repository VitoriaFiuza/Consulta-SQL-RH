# Consulta SQL - RH

Este projeto realiza análises de dados de Recursos Humanos (RH) utilizando Python, SQLite e pandas. Os dados são carregados de um arquivo JSON, armazenados em um banco de dados SQLite, e manipulados com consultas SQL para extrair informações úteis, como salário médio por departamento e distribuição de cargos. Visualizações são geradas com matplotlib para facilitar a interpretação dos resultados.

## Objetivo
Demonstrar habilidades em:
- Manipulação de dados JSON com pandas.
- Criação e gerenciamento de banco de dados SQLite.
- Consultas SQL para análise de dados.
- Visualização de dados com matplotlib.

## Estrutura do Projeto
- `rh_data.json`: Dados fictícios de RH (funcionários, cargos, salários, departamentos).
- `main.py`: Script Python que carrega os dados, cria o banco SQLite, executa consultas SQL e gera gráficos.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.

## Pré-requisitos
- **Python**: 3.8 ou superior.
- **Bibliotecas**:
  - pandas
  - matplotlib
  - sqlite3 (incluso no Python)
- Instale as dependências com:
  ```bash
  pip install -r requirements.txt
