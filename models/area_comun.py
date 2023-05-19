from utils.db import db

class Area_comun(db.Model):
    id_area = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))

    def __init__(self, tipo):
        self.tipo = tipo