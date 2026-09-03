from graficos import grafico_nota_por_genero, grafico_quantidade_por_genero, grafico_distribuicao_notas, grafico_nota_vs_popularidade
from tmdb_api import buscar_filmes_populares
from database import salvar_filmes, carregar_filmes

def main():
    print("Buscando filmes na API da TMDB...")
    df = buscar_filmes_populares(paginas=5)

    salvar_filmes(df)

    print("\nCarregando dados do banco de dados...")
    df_banco = carregar_filmes()
    print(df_banco.head())
    

    print("\n--- Nota média por gênero ---")
    print(df_banco.groupby("genero_principal")["vote_average"].mean().sort_values(ascending=False))
    correlacao = df_banco["popularity"].corr(df_banco["vote_average"])
    print(f"\nCorrelação entre popularidade e nota: {correlacao:.2f}")
    grafico_nota_por_genero(df_banco)
    grafico_quantidade_por_genero(df_banco)
    grafico_distribuicao_notas(df_banco)
    grafico_nota_vs_popularidade(df_banco)
if __name__ == "__main__":
    main()