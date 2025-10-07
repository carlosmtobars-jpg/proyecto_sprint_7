import pandas as pd
import plotly.express as px
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Análisis de vehículos en EE.UU.",
    layout="wide",
    page_icon="🚗"
)

st.title("📊 Análisis interactivo de vehículos usados en EE.UU.")
st.write("Explora el conjunto de datos y visualiza patrones en los precios y kilometrajes de los autos.")

# --- CARGAR DATOS ---
car_data = pd.read_csv('vehicles_us.csv')

# --- FILTROS OPCIONALES ---
st.sidebar.header("Filtros")
selected_make = st.sidebar.selectbox(
    "Selecciona una marca:",
    options=["Todas"] + sorted(car_data["model"].dropna().unique().tolist())
)

if selected_make != "Todas":
    car_data = car_data[car_data["model"] == selected_make]

# --- HISTOGRAMA ---
st.subheader("📈 Distribución del kilometraje")

hist_button = st.button("Mostrar histograma")

if hist_button:
    st.write("Histograma del kilometraje (odometer) para los vehículos listados.")

    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=40,  # más bins para detalle
        color_discrete_sequence=["#0083B8"],  # color corporativo
        title="Distribución de kilometraje de vehículos",
    )
    fig.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Cantidad de vehículos",
        title_x=0.5,
        template="plotly_white",
        bargap=0.05
    )
    fig.update_traces(marker_line_color="white", marker_line_width=1)

    st.plotly_chart(fig, use_container_width=True)

# --- DISPERSIÓN ---
st.subheader("💰 Relación entre kilometraje y precio")

scatter_button = st.button("Mostrar gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión que muestra la relación entre el kilometraje y el precio del vehículo.")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model",  # agrega color por modelo
        hover_data=["model", "year"],
        title="Precio vs Kilometraje",
        opacity=0.7,
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Precio (USD)",
        title_x=0.5,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
