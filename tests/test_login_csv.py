import pytest
from pages.login_page import Login_Page

CASOS_LOGIN = [
    ("standard_user", "secret_sauce"),       # Usuario válido
    ("locked_out_user", "secret_sauce"),     # Usuario bloqueado
    ("problem_user", "secret_sauce"),        # Usuario con problemas
    ("usuario_invalido", "clave_erronea")    # Credenciales falsas
]

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion",
CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    login = Login_Page(driver)
    login.abrir()
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.enviar()
    
    if debe_funcionar:
        assert "inventory.html" in driver.current_url
    else:
        assert login.hay_error()   

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    login = Login_Page(driver)
    login.abrir()
    login.completar_usuario("standard_user")
    login.completar_clave("secret_sauce")
    login.enviar()   