import streamlit as st

# Diccionario actualizado con la nueva entidad "Liberbank" y el cambio de nombre de "CCM"
pagas_dict = {
    'UNICAJA': {'num_pagas_base': 20.5},
    'CCM desde 1.994': {'num_pagas_base': 18.5},
    'CAJA EXTREMADURA': {'num_pagas_base': 18.5, 'ajuste': 1.0541},  # Incremento del 5,41%
    'CAJA CANTABRIA': {'num_pagas_base': 20.5, 'ajuste': 0.98},  # Reducción del 2% en el cálculo total
    'CAJASTUR': {'num_pagas_base': 17.5, 'bono_extra': 300},  # Bono adicional de 300 €
    'Liberbank': {'num_pagas_base': 17.5, 'bono_extra': 300}  # Mismos valores que "Cajastur"
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
    
    # Aplicar ajuste de incremento, descuento o bonificación específica para cada entidad
    if 'ajuste' in pagas_dict[entidad]:  # Ajuste de porcentaje (e.g., 5.41%)
        salario_base *= pagas_dict[entidad]['ajuste']
        
    # Calcular salario anual base ajustado
    salario_total_anual = salario_base * num_pagas_base
    
    # Aplicar cualquier bono adicional
    if 'bono_extra' in pagas_dict[entidad]:  # Bonificación fija adicional
        salario_total_anual += pagas_dict[entidad]['bono_extra']
    
    return salario_total_anual

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

    # Mostrar los resultados
    st.write(f"Salario total anual en {entidad}: {salario_total_entidad:.2f} €")
    st.write(f"Salario total anual en Unicaja: {salario_total_unicaja:.2f} €")
    st.write(f"Diferencia ajustada a favor de Unicaja: {diferencia:.2f} €")
