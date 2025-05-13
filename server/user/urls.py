from user.views import *

def register_routes(app):
	app.add_url_rule('/create/', 'create', crear_usuario, methods=['POST'])
	app.add_url_rule('/user/<id>/', 'user', prueva)
	app.add_url_rule('/eliminar/<id>/', 'eliminar', eliminar)
	app.add_url_rule('/session/', 'session', session, methods=['POST'])
