import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Dashboard Macro", layout="wide", page_icon="📈")

# Estilização CSS
st.markdown("""
    <style>
    .metric-card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("📈 Painel de Análise Macroeconômica")
st.markdown("Monitoramento estratégico da relação entre **IPCA** e **Selic**.")

@st.cache_data
def carregar_dados():
    df = pd.read_csv('base_economica_bcb.csv')
    df['data'] = pd.to_datetime(df['data'])
    return df

df = carregar_dados()

# Filtros
st.sidebar.header("Filtros de Análise")
ano_min = int(df['data'].dt.year.min())
ano_max = int(df['data'].dt.year.max())
anos = st.sidebar.slider("Intervalo de anos", ano_min, ano_max, (ano_min, ano_max))

df_filtrado = df[(df['data'].dt.year >= anos[0]) & (df['data'].dt.year <= anos[1])]

# KPIs
col1, col2 = st.columns(2)
with col1:
    st.metric("Selic Média", f"{df_filtrado['selic_mensal'].mean():.2f}%")
with col2:
    st.metric("IPCA Médio", f"{df_filtrado['ipca_mensal'].mean():.2f}%")

# Gráficos
st.markdown("---")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_filtrado['data'], y=df_filtrado['selic_mensal'], name='Selic', line=dict(color='#0052cc')))
fig.add_trace(go.Scatter(x=df_filtrado['data'], y=df_filtrado['ipca_mensal'], name='IPCA', line=dict(color='#ff4b4b')))
st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlação: Selic vs IPCA")
fig_scatter = px.scatter(df_filtrado, x='selic_mensal', y='ipca_mensal', trendline="ols")
st.plotly_chart(fig_scatter, use_container_width=True)

with st.expander("Ver dados brutos"):
    st.dataframe(df_filtrado, use_container_width=True)