import feedparser
import pandas as pd
from datetime import datetime
from urllib.parse import quote

# ==========================================
# TERMO DE BUSCA
# ==========================================

busca = 'Feminicídio Maringá'

# Corrige caracteres especiais na URL
busca_formatada = quote(busca)

# URL RSS Google Notícias
url = (
    f'https://news.google.com/rss/search?q={busca_formatada}'
    f'&hl=pt-BR&gl=BR&ceid=BR:pt-419'
)

print("Buscando notícias...")
print(url)

# ==========================================
# LEITURA DO RSS
# ==========================================

feed = feedparser.parse(url)

# ==========================================
# LISTA DE NOTÍCIAS
# ==========================================

dados = []

for item in feed.entries:

    titulo = item.title
    link = item.link
    publicado = item.get("published", "")
    coletado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dados.append([
        titulo,
        link,
        publicado,
        coletado_em
    ])

# ==========================================
# DATAFRAME COM COLUNAS SEPARADAS
# ==========================================

df = pd.DataFrame(
    dados,
    columns=[
        "titulo",
        "link",
        "publicado",
        "coletado_em"
    ]
)

# ==========================================
# EXPORTAR CSV
# ==========================================

arquivo = "noticias_feminicidio_maringa.csv"

df.to_csv(
    arquivo,
    index=False,
    encoding="utf-8-sig"
)

# ==========================================
# RESULTADO
# ==========================================

print(f"\n✅ {len(df)} notícias encontradas.")
print(f"📁 Arquivo salvo: {arquivo}")

print("\nPrimeiras notícias:\n")
print(df.head())