from utils.db import db

class Predio_seguridad(db.Model):
    id_predio_seguridad = db.Column(db.Integer, primary_key=True)
    id_seguridad = db.Column(db.Integer)
    id_predio = db.Column(db.Integer)
    cantidad_seguridad = db.Column(db.Integer)

    def __init__(self, id_seguridad, id_predio, cantidad_seguridad):
        self.id_seguridad = id_seguridad
        self.id_predio = id_predio
        self.cantidad_seguridad = cantidad_seguridad