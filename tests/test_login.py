from pages.login_page import LoginPage
import pytest

def test_login_exitoso(driver):
    # 1. Navegar
    driver.get("[https://www.saucedemo.com/](https://www.saucedemo.com/)")
    
    # 2. Interactuar
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # 3. Validar (Assert)
    assert "inventory.html" in driver.current_url, "No se redirigió al inventario"

def test_login_fallido(driver):
    driver.get("[https://www.saucedemo.com/](https://www.saucedemo.com/)")
    
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    
    assert "locked out" in login_page.get_error_message()