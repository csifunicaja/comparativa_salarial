# -*- coding: utf-8 -*-
import smtplib
import dns.resolver
import re
import pandas as pd

def check_email(email):
    print(f"Verificando formato del correo: {email}")
    # Step 1: Basic format validation using regular expression
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, email):
        print(f"{email}: Formato inválido.")
        return "Invalid format"
    
    print(f"{email}: Formato válido. Verificando registros MX...")
    # Step 2: Check domain MX records with a timeout
    domain = email.split('@')[1]
    try:
        # Establecemos un límite de tiempo para la consulta DNS (en segundos)
        mx_records = dns.resolver.resolve(domain, 'MX', lifetime=5)
        print(f"{email}: Registros MX encontrados.")
        return "Valid format and has MX records"
    except dns.resolver.Timeout:
        print(f"{email}: La consulta de DNS agotó el tiempo.")
        return "DNS query timed out"
    except dns.resolver.NoAnswer:
        print(f"{email}: No se encontraron registros MX.")
        return "No MX records found"
    except dns.resolver.NXDOMAIN:
        print(f"{email}: Dominio no existe.")
        return "Domain does not exist"
    except Exception as e:
        print(f"{email}: Error inesperado al verificar registros MX - {e}")
        return "Unexpected error during MX check"

def check_emails_from_excel(file_path):
    # Cargar el archivo como Excel
    df = pd.read_excel(file_path, engine='openpyxl')
    print("Columnas encontradas en el archivo Excel:", df.columns)
    
    # Asegurarnos de que la columna de correo está en minúsculas para evitar errores
    df.columns = df.columns.str.lower()
    
    if 'email' not in df.columns:
        return "Error: 'Email' column not found in the Excel file."
    
    # Procesa cada correo y guarda el estado en la columna 'Status'
    df['Status'] = df['email'].apply(check_email)
    df.to_excel("Checked_Emails.xlsx", index=False)
    return "Check completed. Results saved to 'Checked_Emails.xlsx'."

# Ejecutar la función en el archivo de ejemplo
print(check_emails_from_excel("emails_list.xlsx"))
