from utils.db import db

class Predio_area_comun(db.Model):
    id_pred_area = db.Column(db.Integer, primary_key=True)
    id_area = db.Column(db.Integer)
    id_predio = db.Column(db.Integer)
    area = db.Column(db.Float)

    def __init__(self, id_area, id_predio, area):
        self.id_area = id_area
        self.id_predio = id_predio
        self.area = area