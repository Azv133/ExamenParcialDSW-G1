from utils.db import db

class Predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    area = db.Column(db.Float)
    id_tipo = db.Column(db.Integer)
    nro_casas_habitacion = db.Column(db.Integer)
    nro_puertas_acceso = db.Column(db.Integer)
    nro_torres_bloques = db.Column(db.Integer)
    ubicacion = db.Column(db.String(255))

    def __init__ (self, nombre, area, id_tipo, casas, puertas, torres, ubicacion):
        self.nombre = nombre
        self.area = area
        self.id_tipo = id_tipo
        self.nro_casas_habitacion = casas
        self.nro_puertas_acceso = puertas
        self.nro_torres_bloques = torres
        self.ubicacion = ubicacion


