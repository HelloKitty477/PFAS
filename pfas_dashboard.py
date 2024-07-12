import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.express as px

# dashboard page and title creation
st.set_page_config(
    page_title="The semi-closed Urban Water Cycle (UWC) as a planning tool to monitor PFAS pollution",
    page_icon="🚰",  # Utilizza un emoji di rubinetto
    layout="wide"
)
st.markdown('<h1><i class="fas fa-faucet"></i> The semi-closed Urban Water Cycle (UWC) as a planning tool to monitor PFAS pollution</h1>', unsafe_allow_html=True)

sep=';'
df = pd.read_csv('C:\\Users\\Federica\\Python SS_TU\\data.csv', sep=sep)
#st.write(df)
df3 = df.groupby(['substance_id','treatment_id', 'Country']).size().reset_index(name='number of articles')
df_country = df3.groupby('Country')['number of articles'].sum().reset_index()
# Creazione della mappa utilizzando Plotly Express
fig = px.choropleth(df_country,  # DataFrame con i dati
                    locations='Country',  # Colonna con i nomi dei paesi
                    locationmode='country names',  # Modalità di localizzazione basata sul nome del paese
                    color='number of articles',  # Colonna con i dati da colorare sulla mappa
                    hover_name='Country',  # Nome che appare al passaggio del mouse su ogni area
                    color_continuous_scale='RdBu_r',  # Scala dei colori (puoi scegliere diverse colormap)
                    range_color=[0, df_country['number of articles'].max()],  # Range dei colori
                    title='Number of Articles by Country')  # Titolo della mappa


st.plotly_chart(fig)


df_country = df.groupby(['substance_id','Country']).size().reset_index(name='number of articles')
import pandas as pd
import plotly.express as px


df_pie = df_country.groupby('substance_id')['number of articles'].sum().reset_index()
fig_dwt = px.pie(df_pie, values='number of articles', names='substance_id',
             title='Number of Articles by Substance',
             hover_name='substance_id',
             labels={'number_of_articles': 'Number of Articles'},
             color_discrete_sequence=px.colors.sequential.RdBu_r)


fig_dwt.update_layout(
    legend_title='Substance ID',  # Titolo della legenda
    uniformtext_minsize=12,  # Dimensione minima del testo uniforme
    uniformtext_mode='hide'  # Nascondi il testo uniforme se non ci sono spazi sufficienti
)
st.plotly_chart(fig_dwt)



# New pies

dictionary = {'wwtt': 'ww', 'wwt1': 'ww', 'wwt2': 'ww', 'wwfi': 'ww', 
          'dwuv': 'dw', 'dwoz': 'dw', 'wwel': 'ww', 'wwco': 'ww', 
          'npdlg': 'dw', 'npbk': 'dw', 'dwac': 'dw', 'dwco': 'dw', 
          'dwrf': 'dw', 'dwpr': 'dw', 'dwde': 'dw', 'dwna': 'dw', 
          'dwuf': 'dw', 'dwex': 'dw', 'dwcy': 'dw', 'dwae': 'dw', 
          'dwcl': 'dw', 'grpf':'dw'}

df['treatment_id'] = df['treatment_id'].astype(str)
df['treatment_id'] = df['treatment_id'].replace(dictionary)
df = df.rename(columns={'treatment_id': 'matrix'})
df_country = df.groupby(['substance_id','matrix','treatment_name']).size().reset_index(name='number of articles')



df_pie = df_country.groupby(['substance_id','matrix', 'treatment_name'])['number of articles'].sum().reset_index()
df_dw = df_country[df_country['matrix'] == 'dw']
df_ww = df_country[df_country['matrix'] == 'ww']


# Dreanking water Treatments
fig_dw = px.pie(df_dw, values='number of articles', names='substance_id',
             title='Number of Articles for Drinking Water Treatments',
             hover_name='substance_id',
             labels={'number of articles': 'Number of Articles'},
             color_discrete_sequence=px.colors.sequential.RdBu_r)

fig_dw.update_traces(
    hovertemplate='<b>%{label}</b><br>' +
                  'Treatment Name: %{customdata[0]}<br>' +
                  'Number of Articles: %{value}',
    customdata=df_dw['treatment_name']  # Passa il nome del trattamento come customdata
)

fig_dw.update_layout(
    legend_title='Substance ID',  
    uniformtext_minsize=12,  
    uniformtext_mode='hide'  
)

st.plotly_chart(fig_dw)
#Wastewater Treatments

fig_ww = px.pie(df_ww, values='number of articles', names='substance_id',
             title='Number of Articles for Wastewater Treatments',
             hover_name='substance_id',
             labels={'number of articles': 'Number of Articles'},
             color_discrete_sequence=px.colors.sequential.RdBu_r)

fig_ww.update_traces(
    hovertemplate='<b>%{label}</b><br>' +
                  'Treatment Name: %{customdata[0]}<br>' +
                  'Number of Articles: %{value}',
    customdata=df_ww['treatment_name']  # Passa il nome del trattamento come customdata
)

fig_ww.update_layout(
    legend_title='Substance ID',  
    uniformtext_minsize=12,  
    uniformtext_mode='hide'  
)

st.plotly_chart(fig_ww)