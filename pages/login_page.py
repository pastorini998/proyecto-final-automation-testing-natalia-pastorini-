from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = 'https://www.saucedemo.com/'
from selenium.webdriver.common.by import By

# CLASE LOGIN PAGE
class LoginPage:
    #insertar nombre, password y boton login
    _INPUT_NAME = (By.NAME, 'user-name')
    _INPUT_PASSWORD = (By.NAME, 'password')
    _LOGIN_BUTTON = (By.NAME, 'login-button')
    #iniciar driver
    def __init__(self , driver):
        self.driver = driver

    #abrir explradpr
    def open( self):
        self.driver.get(URL)

    def login(self , username , password ):

        #Añadir expera implicita hasta que la accion sea concretada
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()