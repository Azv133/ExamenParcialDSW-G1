from utils.db import db

class Seguridad(db.Model):
    id_seguridad = db.Column(db.Integer, primary_key=True)
    nombre_seguridad = db.Column(db.String(255))
    tipo_seguridad = db.Column(db.Integer)

    def __init__(self, nombre_seguridad, tipo_seguridad):
        self.nombre_seguridad = nombre_seguridad
        self.tipo_seguridad = tipo_seguridad