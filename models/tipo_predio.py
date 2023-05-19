from utils.db import db

class Tipo_predio(db.Model):
    id_tipo = db.Column(db.Integer, primary_key=True)
    tipo_pred = db.Column(db.String(255))

    def __init__(self, tipo_pred):
        self.tipo_pred = tipo_pred