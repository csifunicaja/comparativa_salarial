import streamlit as st

# Predefined dictionaries from extracted Excel data
# Incluye el ajuste del 5,41% para Caja de Extremadura
pagas_dict = {
    'UNICAJA': {'num_pagas_base': 20.5},
    'CCM': {'num_pagas_base': 18.5},
    'CAJA EXTREMADURA': {'num_pagas_base': 18.5, 'ajuste': 1.0541},  # Incremento del 5,41%
    'CAJA CANTABRIA': {'num_pagas_base': 20.5},
    'CAJASTUR': {'num_pagas_base': 17.5}
}

salario_dict = {
    'NIVEL I': {'salario_mensual': 2829.985},
    'NIVEL II': {'salario_mensual': 2382.6216666666664},
    'NIVEL III': {'salario_mensual': 2114.545},
    'NIVEL IV': {'salario_mensual': 1999.485},
    'NIVEL V': {'salario_mensual': 1935.9025000000001},
    'NIVEL VI': {'salario_mensual': 1872.325},
    'NIVEL VII': {'salario_mensual': 1787.5024999999998},
    'NIVEL VIII': {'salario_mensual': 1727.5525},
    'NIVEL IX': {'salario_mensual': 1637.1966666666667},
    'NIVEL X': {'salario_mensual': 1560.4016666666666},
    'NIVEL XI': {'salario_mensual': 1391.6116666666667},
    'NIVEL XII': {'salario_mensual': 1189.6191666666666},
    'NIVEL XIII': {'salario_mensual': 974.505}
}

# Streamlit interface
st.title("Comparativa Salarial Unicaja")

# Formulario de entrada de datos
st.header("Ingrese sus datos para ver la comparativa salarial")

entidad = st.selectbox("Entidad de Origen", list(pagas_dict.keys()))
nivel = st.selectbox("Nivel/Categoría", list(salario_dict.keys()))

# Función para calcular el salario total sin antigüedad, con ajuste para Caja de Extremadura
def calcular_salario_total(entidad, nivel):
    # Obtener salario base mensual y número de pagas
    salario_base = salario_dict[nivel]['salario_mensual']
    num_pagas_base = pagas_dict[entidad]['num_pagas_base']
    
    # Aplicar ajuste para Caja de Extremadura si existe
    if 'ajuste' in pagas_dict[entidad]:
        salario_base *= pagas_dict[entidad]['ajuste']
    
    # Calcular salario anual total
    salario_total_anual = salario_base * num_pagas_base
    return salario_total_anual

# Botón para calcular la comparativa
if st.button("Calcular Comparativa"):
    salario_total_entidad = calcular_salario_total(entidad, nivel)
    salario_total_unicaja = calcular_salario_total("UNICAJA", nivel)

    # Diferencia salarial con Unicaja
    diferencia = salario_total_unicaja - salario_total_entidad

    # Mostrar los resultados
    st.write(f"Salario total anual en {entidad}: {salario_total_entidad:.2f} €")
    st.write(f"Salario total anual en Unicaja: {salario_total_unicaja:.2f} €")
    st.write(f"Diferencia ajustada a favor de Unicaja: {diferencia:.2f} €")
