import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Carrega o arquivo JSON
data = pd.read_json('rh_data.json')

# Conecta ao banco SQLite (cria se não existir)
conn = sqlite3.connect('rh_database.db')
cursor = conn.cursor()

# Cria a tabela funcionarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        departamento TEXT,
        cargo TEXT,
        salario REAL,
        data_contratacao TEXT
    )
''')

# Insere os dados na tabela
data.to_sql('funcionarios', conn, if_exists='replace', index=False)

# Consulta 1: Salário médio por departamento
query1 = '''
    SELECT departamento, ROUND(AVG(salario), 2) as salario_medio
    FROM funcionarios
    GROUP BY departamento
'''
salario_depto = pd.read_sql_query(query1, conn)
print("\nSalário médio por departamento:")
print(salario_depto)

# Consulta 2: Contagem de funcionários por cargo
query2 = '''
    SELECT cargo, COUNT(*) as quantidade
    FROM funcionarios
    GROUP BY cargo
'''
cargos = pd.read_sql_query(query2, conn)
print("\nContagem de funcionários por cargo:")
print(cargos)

# Consulta 3: Funcionários contratados nos últimos 2 anos
data_limite = (datetime.now() - timedelta(days=2*365)).strftime('%Y-%m-%d')
query3 = f'''
    SELECT nome, data_contratacao
    FROM funcionarios
    WHERE data_contratacao >= '{data_limite}'
'''
recentes = pd.read_sql_query(query3, conn)
print("\nFuncionários contratados nos últimos 2 anos:")
print(recentes)

# Visualização 1: Gráfico de barras - Salário médio por departamento
plt.figure(figsize=(8, 6))
plt.bar(salario_depto['departamento'], salario_depto['salario_medio'], color='skyblue')
plt.title('Salário Médio por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário Médio (R$)')
plt.savefig('salario_por_departamento.png')
plt.close()

# Visualização 2: Gráfico de pizza - Distribuição de cargos
plt.figure(figsize=(8, 6))
plt.pie(cargos['quantidade'], labels=cargos['cargo'], autopct='%1.1f%%')
plt.title('Distribuição de Cargos')
plt.savefig('distribuicao_cargos.png')
plt.close()

# Fecha a conexão
conn.close()