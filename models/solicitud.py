from utils.db import db

class Solicitud(db.Model):
    id_solicitud = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_predio = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    estado = db.Column(db.Integer)
    descripcion = db.Column(db.Text)

    def __init__(self, id_cliente, id_predio, fecha, estado, descripcion):
        self.id_cliente = id_cliente
        self.id_predio = id_predio
        self.fecha = fecha
        self.estado = estado
        self.descripcion = descripcion
    
