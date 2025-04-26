
# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

# Título do dashboard
st.title("Dashboard de Vendas")

# Caminho do arquivo CSV na mesma pasta
csv_file = "sales_data.csv"

# Verifica se o arquivo CSV existe na mesma pasta
if os.path.exists(csv_file):
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(csv_file)

     # Exibe os dados carregados
    st.markdown("### Dados de Vendas Carregados")
    st.dataframe(df.head(10))

      # Conversão da coluna "Date" para formato de data
   
    df['Date_Sold'] = (
        df['Date_Sold'].astype(str)
        .str.replace('-', '/', regex=False)  # Corrigido 'replice' para 'replace'
        .str.strip()
)

# Ajuste no formato de data
    df['Date_Sold'] = pd.to_datetime(df['Date_Sold'], format='%Y/%m/%d')

    # Filtros de seleção
    st.sidebar.header("Filtros")
    selected_store = st.sidebar.multiselect("Nome do produto", options=df['Product_Name'].unique(), default=df['Product_Name'].unique())
    selected_model = st.sidebar.multiselect("Categoria", options=df['Category'].unique(), default=df['Category'].unique())
    selected_date_range = st.sidebar.date_input("Selecione o Período", [df['Date_Sold'].min(), df['Date_Sold'].max()])


    filtered_df = df[(df['Product_Name'].isin(selected_store)) & 
                     (df['Category'].isin(selected_model)) &
                     (df['Date_Sold'] >= pd.to_datetime(selected_date_range[0])) & 
                     (df['Date_Sold'] <= pd.to_datetime(selected_date_range[1]))]

# Exibe os dados filtrados
    st.markdown("### Dados Filtrados")
    st.dataframe(filtered_df)


# Insights gerais
    st.markdown("## Insights Gerais")
    Total_sales = filtered_df['Total_Sales'].sum()
    Quantity_Sold = filtered_df['Quantity_Sold'].sum()
    st.write(f"**Total de Vendas:** R$ {Total_sales:,.2f}")
    st.write(f"**Total de Unidades Vendidas:** {Quantity_Sold}")
    
     # Explicação do Streamlit
    st.markdown("## Sobre o Streamlit")
    st.write("""
    **Streamlit** é uma biblioteca de Python de código aberto que permite criar e compartilhar aplicativos de dados 
    interativos de forma fácil e rápida. Ela transforma scripts em uma interface de usuário web amigável e intuitiva 
    sem a necessidade de conhecimento em desenvolvimento web. Abaixo estão os principais conceitos utilizados neste exemplo:

    - `st.title()`: Adiciona um título ao seu aplicativo.
    - `st.markdown()`: Permite adicionar textos em formato Markdown.
    - `st.dataframe()`: Exibe um DataFrame do Pandas.
    - `st.sidebar`: Permite adicionar componentes de entrada e seleção na barra lateral do aplicativo.
    - `st.multiselect()`: Adiciona uma caixa de seleção múltipla.
    - `st.date_input()`: Adiciona um componente de seleção de data.
    - `st.bar_chart()`: Cria um gráfico de barras.
    - `st.line_chart()`: Cria um gráfico de linha.
    """)

else:
    st.write(f"Arquivo '{csv_file}' não encontrado. Por favor, coloque o arquivo na mesma pasta que este script.")
   