# 📊 Análise Macroeconômica: IPCA & Selic

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

Um pipeline automatizado para extração, processamento e visualização de indicadores estratégicos da economia brasileira. O projeto consome dados diretamente da API do Banco Central do Brasil (BCB) para analisar a relação histórica entre a inflação (IPCA) e a taxa básica de juros (Selic).

---

## 🚀 Dashboard Interativo Ao Vivo

O resultado do processamento de dados está disponível em uma aplicação web interativa:

👉 **[Acessar o Dashboard Macroeconômico](https://pxexedbnqglw73e6yevgxb.streamlit.app/)**

---

## 🎯 Principais Funcionalidades

- **Extração Automatizada:** Script configurado para consumir a API pública do BCB, garantindo governança e confiabilidade na origem dos dados.
- **Tratamento de Dados:** Limpeza e estruturação das séries temporais utilizando a biblioteca `pandas`.
- **Visualização de Indicadores:** Interface web responsiva construída com `streamlit` para análise rápida do cenário econômico.
- **Análise Estratégica:** Documentação complementar com o diagnóstico das tendências e impactos na tomada de decisão. Leia a análise completa no arquivo [`analise_economica.md`](./analise_economica.md).

---

## 📂 Estrutura do Projeto

* `extracao_bcb.py`: Script de integração e requisição à API do Banco Central.
* `main.py` / `app.py`: Código-fonte da aplicação web em Streamlit.
* `base_economica_bcb.csv`: Base de dados estruturada e processada.
* `requirements.txt`: Mapeamento de dependências para o deploy contínuo.
* `analise_economica.md`: Relatório de inteligência focado na interpretação dos indicadores.

---

## 🛠️ Como executar localmente

Caso queira clonar o repositório e rodar o projeto na sua máquina:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/P4mm/Analise_Macro_Economica.git](https://github.com/P4mm/Analise_Macro_Economica.git)
