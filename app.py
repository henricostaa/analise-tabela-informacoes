import streamlit as st
import pandas as pd

st.title("Dashboard de Análise de Logins")

@st.cache_data
def load_data():
    df = pd.read_csv("informacoes.csv")

    # Converter tipos de dados
    df["ultimo_login"] = pd.to_datetime(df["ultimo_login"], errors="coerce")
    df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce")

    # Remover duplicados
    df = df.drop_duplicates()

    return df

df = load_data()

st.sidebar.title("Filtros")

# Filtro por cidade
cidades = df["cidade"].dropna().unique().tolist()
cidades.sort()
cidade_selecionada = st.sidebar.multiselect(
    "Selecione a(s) cidade(s)",
    options=cidades,
    default=cidades
)

# Filtro por gênero
generos = df["genero"].dropna().unique().tolist()
generos.sort()
genero_selecionado = st.sidebar.multiselect(
    "Selecione o(s) gênero(s)",
    options=generos,
    default=generos
)

# Filtro de mês
ordem_mes = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

meses = df["data_nascimento"].dropna().dt.month_name().unique().tolist()
meses.sort(key=lambda x: ordem_mes.index(x))
mes_selecionado = st.sidebar.multiselect(
    "Selecione o(s) mês(es) de aniversário",
    options=meses,
    default=meses
)

df_filtrado = df.copy()

if cidade_selecionada:
    df_filtrado = df_filtrado[df_filtrado["cidade"].isin(cidade_selecionada)]

if mes_selecionado:
    df_filtrado = df_filtrado[df_filtrado["data_nascimento"].dt.month_name().isin(mes_selecionado)]

if genero_selecionado:
    df_filtrado = df_filtrado[df_filtrado["genero"].isin(genero_selecionado)]

st.subheader("Métricas Gerais")

col1, col2, col3 = st.columns(3)

col1.metric("Total de usuários", df_filtrado.shape[0])
col2.metric("Cidades", df_filtrado["cidade"].nunique())
col3.metric("Gêneros", df_filtrado["genero"].nunique())

st.divider()

st.subheader("Logins por Cidade")

df_cidade = (
    df_filtrado.groupby("cidade")["ultimo_login"]
    .count()
    .reset_index()
    .dropna()
    .sort_values(by="ultimo_login", ascending=False)
)

st.bar_chart(df_cidade.head(5), x="cidade", y="ultimo_login", use_container_width=True, x_label="Cidade", y_label="Logins")

st.divider()

st.subheader("Logins por Gênero")

df_genero = (
    df_filtrado.groupby("genero")["ultimo_login"]
    .count()
    .reset_index()
    .dropna()
    .sort_values(by="ultimo_login", ascending=False)
)

st.bar_chart(df_genero, x="genero", y="ultimo_login", use_container_width=True, x_label="Gênero", y_label="Logins")

st.divider()

st.subheader("Aniversários por Mês")

df_niver = df_filtrado.dropna(subset=["data_nascimento"]).copy()
df_niver["mes"] = df_niver["data_nascimento"].dt.month_name()

df_niver["mes"] = pd.Categorical(df_niver["mes"], categories=ordem_mes, ordered=True)

df_mes = (
    df_niver.groupby("mes")
    .size()
    .reset_index(name="aniversarios")
)

st.bar_chart(df_mes, x="mes", y="aniversarios", use_container_width=True, x_label="Mês", y_label="Aniversários")

st.divider()