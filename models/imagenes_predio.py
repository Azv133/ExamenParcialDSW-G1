from utils.db import db

class Imagenes_predio(db.Model):
    id_image = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer)
    nombre_image = db.Column(db.String(255))
    imagen = db.Column(db.LargeBinary(255))

    def __init__(self, id_predio, nombre_image, imagen):
        self.id_predio = id_predio
        self.nombre_image = nombre_image
        self.imagen = imagen