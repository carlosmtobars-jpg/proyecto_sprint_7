# Proyecto_Sprint_7
## Análisis Interactivo de Vehículos Usados en EE.UU.

### Descripción del proyecto
Este proyecto consiste en una aplicación web interactiva desarrollada con **Streamlit**, que permite explorar y visualizar datos de anuncios de vehículos usados en Estados Unidos.  
La aplicación ofrece herramientas visuales para analizar la distribución del kilometraje y la relación entre el precio y el uso del vehículo.  
Su objetivo es facilitar la comprensión de las tendencias del mercado automotriz de segunda mano mediante gráficos dinámicos, intuitivos y personalizables.

---

### Lo que hicimos
- Implementamos la carga de datos desde el archivo `vehicles_us.csv`.  
- Diseñamos una interfaz web con Streamlit, organizada en secciones claras y con un diseño limpio y profesional.  
- Agregamos dos visualizaciones interactivas utilizando Plotly Express:
  - Histograma del kilometraje (odometer) para observar la distribución del uso de los vehículos.
  - Gráfico de dispersión (odometer vs price) para analizar la relación entre kilometraje y precio.  
- Mejoramos la estética de los gráficos aplicando paletas de color coherentes, títulos centrados y el tema `plotly_white`.  
- Incorporamos un filtro lateral (sidebar) que permite seleccionar una marca o modelo específico para un análisis más enfocado.  
- Ajustamos etiquetas, títulos y estilos para ofrecer una experiencia visual más clara y profesional.  
- Corregimos los nombres de columnas y optimizamos el código para garantizar su funcionamiento estable en entornos como Render o GitHub.

---

### Tecnologías utilizadas
- Python  
- Streamlit  
- Pandas  
- Plotly Express
