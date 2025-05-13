from pathlib import Path

def mostrar_estructura(directorio: str, nivel=0):
    ruta = Path(directorio)
    if not ruta.exists() or not ruta.is_dir():
        print(f"{directorio} no es un directorio válido.")
        return
    
    for item in ruta.iterdir():
        prefijo = "│   " * nivel + "├── " if item.is_dir() else "│   " * nivel + "└── "
        print(prefijo + item.name)
        if item.is_dir():
            mostrar_estructura(item, nivel + 1)

# Cambia 'ruta/de/tu/carpeta' por el directorio que quieras inspeccionar
directorio = Path.cwd()  # Esto toma la ruta actual
mostrar_estructura(directorio)
