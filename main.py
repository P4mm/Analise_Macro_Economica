import pandas as pd
import requests
import os

def extrair_dados_bcb(codigo_serie, nome_coluna):
    """Extrai dados da API do Banco Central."""
    print(f"Extraindo: {nome_coluna}...")
    url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json'
    resposta = requests.get(url)
    
    df = pd.DataFrame(resposta.json())
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'])
    return df.rename(columns={'valor': nome_coluna}).set_index('data')

def executar_pipeline():
    # 1. Extração
    df_ipca = extrair_dados_bcb(433, 'ipca_mensal')
    df_selic = extrair_dados_bcb(4390, 'selic_mensal')

    # 2. Transformação (Cruzamento)
    print("Consolidando dados...")
    df_consolidado = pd.merge(df_ipca, df_selic, left_index=True, right_index=True, how='inner')
    df_consolidado = df_consolidado.reset_index()

    # 3. Carga (Salvando CSV na pasta do projeto)
    caminho_arquivo = 'base_economica_bcb.csv'
    df_consolidado.to_csv(caminho_arquivo, index=False, encoding='utf-8')
    
    print(f"\nSucesso! Arquivo gerado em: {os.path.abspath(caminho_arquivo)}")

if __name__ == "__main__":
    executar_pipeline()