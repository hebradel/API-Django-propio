from pathlib import Path
from importlib import import_module

def veri(INSTALLED_APPS):
    for app in INSTALLED_APPS:
        url = Path(f'{Path.cwd()}/{app}')
        init_file = url / '__init__.py'
        db_file = url / 'db.py'
        views_file = url / 'views.py'
        urls_file = url / 'urls.py'
        
        if url.exists():
            if not init_file.exists():
                init_file.touch()
            print('hola')
        else:
            url.mkdir(parents=True, exist_ok=True)
            init_file.write_text("\t# Archivo __init__.py\n")
            db_file.write_text(
                f'from apps.fun.Model import *\n'
                f'#class User(Model):\n'
                f'\t#id = AutoField(primary_key=True)\n'
                f'\t#nombre = CharField(max_length=45, null=True, blank=True)\n'
                f'\t#def __str__(self):\n'
                f'\t\t#return self.nombre or self.id\n'
            )
            views_file.write_text(f"from flask import jsonify\n\ndef prueva():\n\treturn 'hola mundo desde {app}'")
            urls_file.write_text(
                f'from {app}.views import *\n\n'
                f'def register_routes(app):\n'
                f'\tapp.add_url_rule(\'/{app}/\', \'{app}_prueva\', prueva)\n'
            )
            print('creado')

def db_create(installed_apps):
    for app in installed_apps:
        try:
            module = import_module(f"{app}.db")
            if hasattr(module, 'create_tables'):
                module.create_tables()
                print(f" * Tablas creadas para {app}")
            else:
                print(f" * Advertencia: {app}.db no tiene una función create_tables()")
        except ModuleNotFoundError:
            print(f" * Advertencia: No se encontró el módulo {app}.db")