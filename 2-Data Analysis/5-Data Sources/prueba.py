from msilib.schema import CheckBox, RadioButton
from tabnanny import check
import streamlit as st
import pandas as pd


df = pd.read_csv("bicis.csv")


menu_lateral = st.sidebar.selectbox('Sevici Visualization app',['Datos','Visualizacion','filtrado'])


# if menu_lateral=='Home':
#     st.title("Esto es una prueba")

# with st.expander("pulsame"):
    

# CheckBox = st.checkbox('Click y suma 1')

# if CheckBox:
#     st.markdown ("me has clicado")

# st.sidebar.image((logo_path="foto_bici.jpeg", width=50, height=60))

if menu_lateral == "Datos":
    st.title(" Datos de Sevici")
    st.metric('Distrito', df['capacity'].sum(), delta=20, delta_color="normal", help=None)
    df
elif menu_lateral == "Visualizacion":
    st.title("Mapa de Bicis")
    st.map(data=df, zoom=None, use_container_width=True)
elif menu_lateral=='filtrado':
     menu_radio=st.sidebar.radio('Seleccione una opción de filtro',('calle','Capacidad & Distrito'))
     makes = df['name'].drop_duplicates()
     make_choice = st.sidebar.selectbox('Seleccione calle:', makes)
     



