import bcrypt
def encriptar_contraseña(password):
    # Generar un salt y encriptar la contraseña
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verificar_contraseña(password, hashed_password):
    # Verificar si la contraseña proporcionada coincide con el hash guardado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)