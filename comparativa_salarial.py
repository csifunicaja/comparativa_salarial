import streamlit as st

# Predefined dictionaries from extracted Excel data
pagas_dict = {
    'UNICAJA': {'num_pagas_base': 20.5, 'num_pagas_trienios': 12.0},
    'CCM': {'num_pagas_base': 18.5, 'num_pagas_trienios': 18.5},
    'CAJA EXTREMADURA': {'num_pagas_base': 18.5, 'num_pagas_trienios': 18.5},
    'CAJA CANTABRIA': {'num_pagas_base': 20.5, 'num_pagas_trienios': 19.5},
    'CAJASTUR': {'num_pagas_base': 17.5, 'num_pagas_trienios': 12.0}
}

salario_dict = {
    'NIVEL I': {'salario_anual': 33959.82, 'salario_mensual': 2829.985},
    'NIVEL II': {'salario_anual': 28591.46, 'salario_mensual': 2382.6216666666664},
    'NIVEL III': {'salario_anual': 25374.54, 'salario_mensual': 2114.545},
    'NIVEL IV': {'salario_anual': 23993.82, 'salario_mensual': 1999.485},
    'NIVEL V': {'salario_anual': 23230.83, 'salario_mensual': 1935.9025000000001},
    'NIVEL VI': {'salario_anual': 22467.9, 'salario_mensual': 1872.325},
    'NIVEL VII': {'salario_anual': 21450.03, 'salario_mensual': 1787.5024999999998},
    'NIVEL VIII': {'salario_anual': 20730.63, 'salario_mensual': 1727.5525},
    'NIVEL IX': {'salario_anual': 19646.36, 'salario_mensual': 1637.1966666666667},
    'NIVEL X': {'salario_anual': 18724.82, 'salario_mensual': 1560.4016666666666},
    'NIVEL XI': {'salario_anual': 16699.34, 'salario_mensual': 1391.6116666666667},
    'NIVEL XII': {'salario_anual': 14275.43, 'salario_mensual': 1189.6191666666666},
    'NIVEL XIII': {'salario_anual': 11694.06, 'salario_mensual': 974.505}
}

# Streamlit interface
st.title("Comparativa Salarial Unicaja")

# Formulario de entrada de datos
st.header("Ingrese sus datos para ver la comparativa salarial")

entidad = st.selectbox("Entidad de Origen", list(pagas_dict.keys()))
nivel = st.selectbox("Nivel/Categoría", list(salario_dict.keys()))
trienios = st.number_input("Trienios (años de antigüedad)", min_value=0)

# Función para calcular el salario total con trienios ajustado al número de pagas de la entidad
def calcular_salario_total(entidad, nivel, trienios):
    # Datos de salario base y pagas
    salario_base = salario_dict[nivel]['salario_mensual']
    num_pagas_base = pagas_dict[entidad]['num_pagas_base']
    num_pagas_trienios = pagas_dict[entidad]['num_pagas_trienios']
    
    # Calcular salario anual base
    salario_anual_base = salario_base * num_pagas_base
    
    # Calcular incremento de trienios ajustado
    incremento_trienio = salario_base * 0.04 * num_pagas_trienios
    total_antiguedad = trienios * incremento_trienio
    
    # Salario total anual ajustado
    salario_total_anual = salario_anual_base + total_antiguedad
    return salario_total_anual

# Botón para calcular la comparativa
if st.button("Calcular Comparativa"):
    salario_total_entidad = calcular_salario_total(entidad, nivel, trienios)
    salario_total_unicaja = calcular_salario_total("UNICAJA", nivel, trienios)

    # Diferencia salarial con Unicaja
    diferencia = salario_total_unicaja - salario_total_entidad

    # Mostrar los resultados
    st.write(f"Salario total anual en {entidad}: {salario_total_entidad:.2f} €")
    st.write(f"Salario total anual en Unicaja: {salario_total_unicaja:.2f} €")
    st.write(f"Diferencia ajustada a favor de Unicaja: {diferencia:.2f} €")
