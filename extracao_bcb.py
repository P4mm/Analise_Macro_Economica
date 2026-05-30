import pandas as pd
import requests

def extrair_dados_bcb(codigo_serie, nome_coluna):
    """
    Conecta na API do Banco Central e extrai a série histórica.
    """
    print(f"Buscando dados da série {codigo_serie} ({nome_coluna})...")
    url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json'
    
    # Faz a requisição na API
    resposta = requests.get(url)
    
    # Converte o resultado (JSON) para um DataFrame do Pandas
    df = pd.DataFrame(resposta.json())
    
    # Limpeza e Formatação Básica
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'])
    
    # Renomeia a coluna 'valor' para o nome do indicador
    df = df.rename(columns={'valor': nome_coluna})
    
    # Define a data como índice para facilitar cruzamento de dados depois
    df = df.set_index('data')
    return df

# 1. Extraindo a Inflação (IPCA mensal - Código 433)
df_ipca = extrair_dados_bcb(433, 'ipca_mensal')

# 2. Extraindo a Taxa de Juros (Selic mensal - Código 4390)
df_selic = extrair_dados_bcb(4390, 'selic_mensal')

# 3. Juntando as duas tabelas pela data (Merge)
print("Cruzando os dados...")
df_consolidado = pd.merge(df_ipca, df_selic, left_index=True, right_index=True, how='inner')

# Reseta o índice para a data voltar a ser uma coluna normal
df_consolidado = df_consolidado.reset_index()

# 4. Salvando o arquivo para o Looker Studio
nome_arquivo = 'base_economica_bcb.csv'
df_consolidado.to_csv(nome_arquivo, index=False, encoding='utf-8')

print(f"\nSucesso! Arquivo '{nome_arquivo}' criado na sua pasta.")
print(df_consolidado.tail()) # Mostra as últimas 5 linhas no terminal para você conferir