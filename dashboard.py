import streamlit as st
from database import carregar_filmes
from graficos import grafico_nota_por_genero, grafico_quantidade_por_genero, grafico_distribuicao_notas, grafico_nota_vs_popularidade

st.title("TMDB Analytics 🎬")
st.write("Análise de filmes populares coletados da API do TMDB")
df = carregar_filmes()
generos = df["genero_principal"].unique()
genero_selecionado = st.selectbox("Filtrar por gênero:", options=["Todos"] + list(generos))

if genero_selecionado != "Todos":
    df = df[df["genero_principal"] == genero_selecionado]
st.dataframe(df)

st.subheader("Nota média por gênero")
fig = grafico_nota_por_genero(df)
st.pyplot(fig)

st.subheader("Quantidade de filmes por gênero")
fig2 = grafico_quantidade_por_genero(df)
st.pyplot(fig2)

st.subheader("Distribuição das notas")
fig3 = grafico_distribuicao_notas(df)
st.pyplot(fig3)

st.subheader("Nota vs. Popularidade")
fig4 = grafico_nota_vs_popularidade(df)
st.pyplot(fig4)