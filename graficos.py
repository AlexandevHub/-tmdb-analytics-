import matplotlib.pyplot as plt

def grafico_nota_por_genero(df):
    fig, ax = plt.subplots()
    media_por_genero = df.groupby("genero_principal")["vote_average"].mean().sort_values(ascending=False)
    media_por_genero.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_title("Nota média por gênero")
    ax.set_ylabel("Nota média (vote_average)")
    ax.set_xlabel("Gênero")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig

def grafico_quantidade_por_genero(df):
    fig, ax = plt.subplots()
    quantidade_por_genero = df["genero_principal"].value_counts()
    quantidade_por_genero.plot(kind="bar", color="salmon", ax=ax)
    ax.set_title("Quantidade de filmes por gênero")
    ax.set_ylabel("Número de filmes")
    ax.set_xlabel("Gênero")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig

def grafico_distribuicao_notas(df):
    fig, ax = plt.subplots()
    df["vote_average"].plot(kind="hist", bins=10, color="mediumseagreen", edgecolor="black", ax=ax)
    ax.set_title("Distribuição das notas dos filmes")
    ax.set_xlabel("Nota (vote_average)")
    ax.set_ylabel("Quantidade de filmes")
    plt.tight_layout()
    return fig

def grafico_nota_vs_popularidade(df):
    fig, ax = plt.subplots()
    ax.scatter(df["popularity"], df["vote_average"], alpha=0.6, color="darkorange")
    ax.set_title("Nota vs. Popularidade")
    ax.set_xlabel("Popularidade")
    ax.set_ylabel("Nota (vote_average)")
    plt.tight_layout()
    return fig