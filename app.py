# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:42:06 2024

@author: jperezr
"""

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Chiles En Nogada - ¡No te lo pierdas!", layout="centered")

# Mostrar la imagen al inicio
st.image("nogada.jpg", caption="Chiles en Nogada", use_column_width=True)

# Título
st.title("¡Dios te bendiga!")

# Mensaje principal con texto grande
st.markdown("""
    <div style="font-size: 24px; text-align: center;">
        <strong>No te pierdas de esta delicia de "Chiles en Nogada" preparados con mi receta original.</strong><br><br>
        Siempre imitados, jamás igualados...<br><br>
        <strong>Sábado 3 de agosto 3 PM.</strong><br><br>
        Entrega en 3a Privada de Reforma Ocotlán, Tlax.<br><br>
        ¡Haz tus pedidos ya! 🌶🌶🌶🥬🫛🥦🫛🥬<br><br>
        <strong>Costo: $130</strong>, incluye una exquisita guarnición de espagueti.<br><br>
        Lleva tus topers. Y por favor, comparte mi publicación. ¡Gracias!
    </div>
""", unsafe_allow_html=True)

# Añadir un botón de contacto o formulario (opcional)
st.write("Para realizar tu pedido, puedes contactarme al número [246 159 3018].")

# Botón para compartir en redes sociales (opcional, solo texto por ahora)
st.write("¡Comparte esta publicación con tus amigos!")

# Agregar estilos adicionales (opcional)
st.markdown("""
    <style>
    .main {
        color: #4CAF50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
