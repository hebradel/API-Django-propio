from flask import jsonify, request
from user.db import *
from apps.fun.password import *

def prueva(id):
    us = User.get(id=id)
    if not us:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    # Convertir el objeto User a un diccionario
    user_data = {
        field: (getattr(us, field).decode() if isinstance(getattr(us, field), bytes) else getattr(us, field))
        for field in us._fields.keys()
    }
    
    return jsonify(user_data), 200


def eliminar(id):
    us = User.get(id=id)
    
    if not us:
        return jsonify({"error": "El usuario no existe"}), 404
    
    nombre = us.nombre
    us.delete()
    
    return jsonify({"msg": f"El usuario '{nombre}' fue eliminado"}), 200

def crear_usuario():
    data = request.get_json()  # Obtener los datos en formato JSON
    nombre = data.get("nombre", "")
    password = data.get("password", "")
    
    if nombre and password:
        password_hash = encriptar_contraseña(password)
        us = User(nombre=nombre, password=password_hash)
        us.save()
        return jsonify({"message": "Usuario creado", "id": us.id, "nombre": us.nombre}), 201
    else:
        return jsonify({"error": "El nombre es requerido"}), 400
    
def session():
    data = request.get_json()
    nombre = data.get("nombre", "")
    password = data.get("password", "")
    
    if nombre and password:
        us = User.get(nombre=nombre)
        if us and verificar_contraseña(password, us.password):
            return jsonify({"message": "Inicio de sesión exitoso", "id": us.id, "nombre": us.nombre}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 400
    else:
        return jsonify({"error": "El nombre y la contraseña son requeridos"}), 400
