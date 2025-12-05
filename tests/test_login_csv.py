import pytest
from pages.login_page import LoginPage #recibe info de logueo

CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True, "Usuario valido"),
    ("locked_out_user", "secret_sauce", False, "Usuario bloqueado"),
    ("problem_user", "secret_sauce", True, "Problema visual"),
    ("usuario_invalido", "clave_erronea", False, "Datos invalidos")
]

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    
    login = LoginPage(driver)
    login.click()
    
    # Logueo usuario contraseña click button
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.click_login()
    
    #Validación
    if debe_funcionar:
        assert "inventory.html" in driver.current_url, f"Fallo: {descripcion}"
    else:
        error = login.obtener_mensaje_error()
        assert "sadface" in error, f"El mensaje de error no fue el esperado. Recibido: {error}"

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario("standard_user")
    login.completar_clave("secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url