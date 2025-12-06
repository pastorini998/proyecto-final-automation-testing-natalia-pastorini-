import pytest
import pathlib
import pytest_html # <--- Esta era la línea faltante
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

# --- Hook para Capturas de Pantalla en Reporte HTML ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Crear carpeta reports/screens si no existe
            target_dir = pathlib.Path("reports/screens")
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Guardar captura
            file_name = target_dir / f"{item.name}.png"
            driver.save_screenshot(str(file_name))
            
            # Adjuntar al reporte HTML
            if hasattr(report, 'extra'):
                # Ahora sí funcionará esta línea
                report.extra.append(pytest_html.extras.image(str(file_name)))