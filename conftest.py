import pytest
import time
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# FIXTURE DEL DRIVER 
@pytest.fixture(scope="function")
def driver():
    """
    Configura el navegador Chrome antes de cada test.
    Se ejecuta automáticamente al pedir 'driver' en los tests.
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--start-maximized") # Maximizar ventana
    
    # Inicia Chrome
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Espera implícita
    driver.implicitly_wait(5)
    
    yield driver  # Entrega el control al test
    
    #Cerrar Chrome después del test
    driver.quit()

# --- HOOK PARA SCREENSHOTS (Clase 13) ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Toma una captura de pantalla automáticamente si un test falla    """
    outcome = yield
    report = outcome.get_result()
    
    # Si el test falló en la etapa de ejecución ('call')
    if report.when == 'call' and report.failed:
        # Busca el driver dentro del test
        driver = item.funcargs.get('driver')
        if driver:
            # Crea la carpeta de reportes si no existe
            report_dir = pathlib.Path('reports/screens')
            report_dir.mkdir(parents=True, exist_ok=True)
            
            # Nombre del archivo basado en el nombre del test
            file_name = report_dir / f"{item.name}.png"
            driver.save_screenshot(str(file_name))
            
            # Adjunta al reporte HTML
            if hasattr(report, 'extra'):
                report.extra.append({'name': 'Screenshot', 'format': 'image', 'content': str(file_name)})