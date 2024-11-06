import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

usuario = 'postgres'
senha = quote_plus('@manaus')  # Codifica '@' e outros caracteres especiais
host = 'localhost'
porta = '5432'
nome_db = 'db_financeiro'

# String de conexão atualizada
url_conexao = f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{nome_db}'

# Conectando ao banco
engine = create_engine(url_conexao, client_encoding="utf8")

# 1. Carregar a planilha
file_path = r'C:\Users\Paulo\Documents\Financeiro\Controle-Financeiro.xlsx'
df = pd.read_excel(file_path, sheet_name='Outubro')  # Altere 'Outubro' conforme necessário

# 2. Inserir os dados no banco de dados
tabela_destino = 'outubro'
df.to_sql(tabela_destino, engine, if_exists='replace', index=False)

print("Dados carregados com sucesso!")
