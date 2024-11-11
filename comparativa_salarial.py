import streamlit as st

# Configura el título de la página y el ícono en la pestaña del navegador
st.set_page_config(page_title="Comparativa Salarial Unicaja", page_icon="💼")

st.image("https://drive.google.com/file/d/1qkYxyl0lPql_euR7vdBqFdAkgGvJua56/view?usp=sharing", width=200)


# Diccionario actualizado con las configuraciones específicas para cada entidad de origen
pagas_dict = {
    'UNICAJA': {'num_pagas_base': 20.5},
    'CCM desde 1.994': {'num_pagas_base': 18.5},
    'CAJA EXTREMADURA': {'num_pagas_base': 18.5, 'ajuste': 1.0541},  # Incremento del 5.41%
    'CAJA CANTABRIA': {'num_pagas_base': 20.5},
    'CAJASTUR': {'num_pagas_base': 17.5},
    'Liberbank': {'num_pagas_base': 17.5}  # Mismos valores que "Cajastur"
}

# Incluye todos los niveles hasta NIVEL XIII
salario_dict = {
    'NIVEL I': {'salario_mensual': 2829.985},
    'NIVEL II': {'salario_mensual': 2382.6216666666664},
    'NIVEL III': {'salario_mensual': 2114.545},
    'NIVEL IV': {'salario_mensual': 1999.485},
    'NIVEL V': {'salario_mensual': 1935.9025},
    'NIVEL VI': {'salario_mensual': 1872.325},
    'NIVEL VII': {'salario_mensual': 1787.5025},
    'NIVEL VIII': {'salario_mensual': 1727.5525},
    'NIVEL IX': {'salario_mensual': 1637.1966666666667},
    'NIVEL X': {'salario_mensual': 1560.4016666666666},
    'NIVEL XI': {'salario_mensual': 1391.6116666666667},
    'NIVEL XII': {'salario_mensual': 1189.6191666666666},
    'NIVEL XIII': {'salario_mensual': 974.505}
}

# Función para calcular el salario total ajustado con parámetros específicos
def calcular_salario_total(entidad, nivel):
    # Obtener salario base mensual y número de pagas
    salario_base = salario_dict[nivel]['salario_mensual']
    num_pagas_base = pagas_dict[entidad]['num_pagas_base']
    
    # Aplicar ajuste de incremento específico para Caja Extremadura
    if 'ajuste' in pagas_dict[entidad]:  # Ajuste del 5.41% si existe
        salario_base *= pagas_dict[entidad]['ajuste']
        
    # Calcular salario anual base ajustado
    salario_total_anual = salario_base * num_pagas_base
    return salario_total_anual

# Función para formatear números al estilo europeo
def formatear_europeo(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Interfaz de usuario con Streamlit
st.title("Comparativa Salarial Unicaja")

# Formulario de entrada de datos
st.header("Ingrese sus datos para ver la comparativa salarial")

entidad = st.selectbox("Entidad de Origen", list(pagas_dict.keys()))
nivel = st.selectbox("Nivel/Categoría", list(salario_dict.keys()))

# Botón para calcular la comparativa
if st.button("Calcular Comparativa"):
    salario_total_entidad = calcular_salario_total(entidad, nivel)
    salario_total_unicaja = calcular_salario_total("UNICAJA", nivel)

    # Diferencia salarial con Unicaja
    diferencia = salario_total_unicaja - salario_total_entidad

    # Mostrar los resultados con formato europeo
    st.write(f"**Salario total anual en {entidad}:** {formatear_europeo(salario_total_entidad)} €")
    st.write(f"**Salario total anual en Unicaja:** {formatear_europeo(salario_total_unicaja)} €")

    # Texto de diferencia en un recuadro resaltado y centrado
    st.markdown(f"""
        <div style='text-align: center; margin-top: 20px;'>
            <div style='display: inline-block; padding: 15px; background-color: #f0f0f5; border-radius: 10px; width: 80%;'>
                <h3 style='color: #333; font-weight: bold;'>Diferencia ajustada a favor de Unicaja: {formatear_europeo(diferencia)} €</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Texto adicional centrado con estilo
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #555555;'>Comparativa calculada sobre Salario Base y número de pagas anuales con importe de 2024.</h5>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px; color: #777777;'>La diferencia retributiva es acumulable anualmente, en 2023 la cantidad es la misma.</p>", unsafe_allow_html=True)
