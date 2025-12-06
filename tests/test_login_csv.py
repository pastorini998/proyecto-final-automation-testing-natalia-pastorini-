import pytest
import csv
from pages.login_page import LoginPage

# --- Función para leer el CSV ---
def obtener_datos_csv():
    datos = []
    try:
        with open('login.csv', newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile)
            next(lector) 
            for fila in lector:
                # fila = [usuario, clave, resultado, descripcion]
                es_valido = fila[4] == "True"  # Convertir texto a booleano
                datos.append((fila, fila[1], es_valido, fila[5]))
    except FileNotFoundError:
        print("ERROR: No se encuentra el archivo login.csv")
    return datos

@pytest.mark.smoke
@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", obtener_datos_csv())
def test_login_csv(driver, usuario, clave, debe_funcionar, descripcion):
    # 1. Instanciar y abrir
    login = LoginPage(driver)
    login.abrir()
    
    # 2. Acciones
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.click_login()
    
    # 3. Validaciones
    if debe_funcionar:
        assert "inventory.html" in driver.current_url, f"Fallo login valido: {descripcion}"
    else:
        error = login.obtener_mensaje_error()
        # Buscamos 'sadface' (error genérico) o 'locked out' (usuario bloqueado)
        assert "sadface" in error or "locked out" in error, f"Error inesperado: {error}"