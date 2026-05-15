# Coletor de Notícias sobre Feminicídio em Maringá

## Descrição

Este projeto realiza a coleta automática de notícias relacionadas a:

* **Feminicídio**
* **Maringá**

utilizando o RSS do Google Notícias.

Os dados coletados são exportados para um arquivo `.csv`, permitindo análises acadêmicas, estatísticas e jurídicas.

---

# Objetivo

O script foi desenvolvido para auxiliar pesquisas acadêmicas, especialmente:

* TCCs;
* artigos científicos;
* pesquisas em Direito;
* estudos de violência de gênero;
* análise de dados criminais;
* mapeamento de casos de feminicídio.

---

# Tecnologias Utilizadas

* Python 3
* feedparser
* pandas

---

# Estrutura dos Dados

O arquivo CSV gerado possui as seguintes colunas:

| Coluna      | Descrição             |
| ----------- | --------------------- |
| titulo      | Título da notícia     |
| link        | Link da notícia       |
| publicado   | Data de publicação    |
| coletado_em | Data e hora da coleta |

---

# Instalação

## 1. Instale o Python

Baixe em:

[Python Oficial](https://www.python.org/downloads/?utm_source=chatgpt.com)

Durante a instalação:

* marque a opção **Add Python to PATH**

---

## 2. Instale as dependências

Abra o terminal na pasta do projeto e execute:

```bash id="9s2h1a"
pip install pandas feedparser
```

---

# Como Executar

No terminal:

```bash id="f4n7z2"
python noticias_feminicidio_maringa.py
```

---

# Resultado

O script criará automaticamente o arquivo:

```txt id="b7k3d1"
noticias_feminicidio_maringa.csv
```

---

# Exemplo de Saída

| titulo                            | link        | publicado        | coletado_em         |
| --------------------------------- | ----------- | ---------------- | ------------------- |
| Caso de feminicídio em Maringá... | https://... | Tue, 14 May 2026 | 2026-05-14 10:30:00 |

---

# Estrutura do Projeto

```txt id="w1x8m4"
projeto/
│
├── noticias_feminicidio_maringa.py
├── noticias_feminicidio_maringa.csv
└── README.md
```

---

# Possíveis Melhorias

O projeto pode ser expandido para:

* coleta automática diária;
* integração com banco de dados;
* dashboard em Power BI;
* análise de sentimentos;
* geolocalização dos casos;
* geração de gráficos;
* coleta de decisões judiciais do TJPR;
* cruzamento com dados do Ministério Público e Segurança Pública.

---

# Observação

As notícias são coletadas através do RSS público do Google Notícias.

A disponibilidade dos resultados depende:

* da indexação do Google;
* da existência de notícias públicas relacionadas ao tema.

---

# Autora

**Eloisa Potrich**
Projeto acadêmico voltado à pesquisa em Direito e análise de dados sobre feminicídio em Maringá/PR.
