from importlib import import_module
from apps.settings import INSTALLED_APPS

def register_urls(app):
    for app_name in INSTALLED_APPS:
        try:
            module = import_module(f"{app_name}.urls")
            module.register_routes(app)
            print(f" * Rutas cargadas para {app_name}")
        except (ModuleNotFoundError, AttributeError):
            print(f" * Advertencia: No se pudieron cargar las rutas para {app_name}")