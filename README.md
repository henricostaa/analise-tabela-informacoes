# Análise de Tabela de Informações

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?logo=streamlit&logoColor=white)](https://analytics-dashboard-info.streamlit.app/)

Dashboard interativo em **Streamlit** para analisar logins recentes, segmentando por cidade, gênero e mês de aniversário. O projeto utiliza um arquivo CSV (`informacoes.csv`) e exibe métricas e gráficos com filtros rápidos.

## Funcionalidades
- Filtros por **cidade**, **gênero** e **mês de aniversário**.
- Métricas gerais (total de usuários, cidades e gêneros).
- Gráficos de barras para:
  - Logins por cidade (top 5).
  - Logins por gênero.
  - Aniversários por mês.

## Estrutura do projeto
```
.
├── app.py              # App Streamlit
├── informacoes.csv     # Base de dados
├── main.ipynb          # Notebook auxiliar
└── README.md
```

## Como executar
1. (Opcional) Crie e ative um ambiente virtual.
2. Instale as dependências:

```bash
pip install streamlit pandas
```

3. Execute o app:

```bash
streamlit run app.py
```

4. Acesse a URL exibida no terminal (geralmente `http://localhost:8501`).

## Dados
O app lê o arquivo `informacoes.csv` e converte colunas de data (`ultimo_login` e `data_nascimento`) para datetime, removendo duplicados antes das análises.
