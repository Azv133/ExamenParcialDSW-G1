from utils.db import db

class Tipo_seguridad(db.Model):
    id_tipo_seg = db.Column(db.Integer, primary_key=True)
    name_tipo_seg = db.Column(db.String(255))

    def __init__(self, name_tipo_seg):
        self.name_tipo_seg = name_tipo_seg