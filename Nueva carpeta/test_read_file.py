# -*- coding: utf-8 -*-
import pandas as pd

def read_file(file_path):
    try:
        # Intentar leer como Excel
        df = pd.read_excel(file_path, engine='openpyxl')
        print("Archivo leído como Excel.")
    except Exception as e:
        print("Error al leer como Excel:", e)
        try:
            # Si falla, intentar como CSV con varias codificaciones
            df = pd.read_csv(file_path, encoding='utf-8')
            print("Archivo leído como CSV con codificación utf-8.")
        except Exception as e_utf8:
            print("Error al leer como CSV utf-8:", e_utf8)
            try:
                df = pd.read_csv(file_path, encoding='latin1')
                print("Archivo leído como CSV con codificación latin1.")
            except Exception as e_latin1:
                print("Error al leer como CSV latin1:", e_latin1)
                try:
                    df = pd.read_csv(file_path, encoding='iso-8859-1')
                    print("Archivo leído como CSV con codificación iso-8859-1.")
                except Exception as e_iso:
                    print("Error al leer como CSV iso-8859-1:", e_iso)
                    return "No se pudo leer el archivo."

    # Mostrar columnas y primeras filas para ver el contenido
    print("Columnas en el archivo:", df.columns)
    print("Primeras filas del archivo:\n", df.head())

# Cambia el nombre del archivo aquí según el tipo de archivo que tengas.
print(read_file("emails_list.xlsx"))
