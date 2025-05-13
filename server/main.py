from flask import Flask
from apps.fun.urls import register_urls
from apps.settings import *
from apps.fun.cosas import *

veri(INSTALLED_APPS)
db_create(INSTALLED_APPS)
app = Flask(__name__)
register_urls(app)

if __name__ == "__main__":
    print(f" * Aplicaciones : {INSTALLED_APPS}")
    app.run(host=HOST, port=PORT, debug=DEBUG)
