def leer_csv_login(ruta_archivo):
    import csv
    from pathlib import Path

    ruta_completa = Path(__file__).parent.parent / ruta_archivo
    casos = []

    with open(ruta_completa, newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            usuario = fila['usuario']
            clave = fila['clave']
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            casos.append((usuario, clave, debe_funcionar))

    return casos

def leer_json_productos(ruta_archivo):
    import json
    from pathlib import Path

    ruta_completa = Path(__file__).parent.parent / ruta_archivo
    with open(ruta_completa) as archivo:
        datos = json.load(archivo)
    
    return datos