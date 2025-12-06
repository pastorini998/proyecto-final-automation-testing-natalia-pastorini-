import pytest
import csv
from pathlib import Path
from pages.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.datos import  leer_csv_login
from utils.faker import get_login_faker
 




@pytest.mark.parametrize("username,password,login_bool",CASOS_LOGIN)
def test_login( driver, username , password , login_bool ):
    #crear objeto (instanciarlo)
    loginPage = LoginPage(driver) 
    loginPage.open()
    loginPage.login(username , password)

    if login_bool:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url
