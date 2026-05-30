import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Análise Macroeconômica", layout="wide")

st.title("📊 Painel de Indicadores Econômicos")
st.write("Análise da relação entre IPCA e Selic - Dados via BCB")

# Carregar os dados
df = pd.read_csv('base_economica_bcb.csv')
df['data'] = pd.to_datetime(df['data'])

# Gráfico
st.line_chart(df.set_index('data')[['ipca_mensal', 'selic_mensal']])

st.write("### Dados Brutos")
st.dataframe(df)