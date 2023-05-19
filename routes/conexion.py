from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.area_comun import Area_comun
from models.cliente import Cliente
from models.estado_solicitud import Estado_solicitud
from models.imagenes_predio import Imagenes_predio
from models.predio_area_comun import Predio_area_comun
from models.predio_seguridad import Predio_seguridad
from models.predio import Predio
from models.seguridad import Seguridad
from models.solicitud import Solicitud
from models.tipo_predio import Tipo_predio
from models.tipo_seguridad import Tipo_seguridad
from utils.db import db
from sqlalchemy import text
from datetime import datetime
import base64

conexion = Blueprint("conexion", __name__)

@conexion.route('/')
def index():
    return redirect(url_for('conexion.solicitarCotizacion'))

@conexion.route('/about')
def about():
    return render_template('about.html')

@conexion.route('/solicitarCotizacion')
def solicitarCotizacion():
    tipo_predio = Tipo_predio.query.all()
    area_comun = Area_comun.query.all()
    tipo_seguridad = Tipo_seguridad.query.all()
    return render_template('solicitarCotizacion.html', tipo_predio = tipo_predio, 
                            area_comun = area_comun, tipo_seguridad = tipo_seguridad)

@conexion.route('/nuevoPredio', methods=['POST'])
def add_predio():
    if request.method == 'POST':

        #Realizamos las inserciones en las tablas de nuestra BD

        #Tabla predio
        nombre = request.form['nombre_predio']
        area = request.form['area_predio']
        tipo = request.form['tipo_predio']
        nro_casas_habitacion = request.form['nro_casas_habitacion']
        nro_puertas_acceso = request.form['nro_puertas_acceso']
        nro_torres_bloques = request.form['nro_torres_bloques']
        ubicacion = request.form['ubicacion']
    
        new_predio = Predio(nombre, area, tipo, nro_casas_habitacion, nro_puertas_acceso, nro_torres_bloques, ubicacion)

        db.session.add(new_predio)
        db.session.commit()
        

        id_predio = new_predio.id_predio

        flash('Predio añadido satisfactoriamente')

        #Tabla seguridad y predio_seguridad
        nombres_s = request.form.getlist('nombre_seguridad')
        tipos_s = request.form.getlist('tipo_seguridad')
        cantidades_seg = request.form.getlist('cantidad_seguridad')


        for i in range(len(nombres_s)):
            if nombres_s[i] != "" and cantidades_seg[i] != 0:
                new_seguridad = Seguridad(nombres_s[i], tipos_s[i])
                db.session.add(new_seguridad)
                db.session.commit()

                new_predio_seguridad = Predio_seguridad(new_seguridad.id_seguridad, id_predio, cantidades_seg[i])
                db.session.add(new_predio_seguridad)
                db.session.commit()
                

        #Tabla predio_area_comun
        ids_area = request.form.getlist('tipo_area_comun')
        areas = request.form.getlist('area_area_comun')

        for j in range(len(ids_area)):
            if areas[j] != "":
                new_predio_area_comun = Predio_area_comun(ids_area[j], id_predio, areas[j])
                db.session.add(new_predio_area_comun)
                db.session.commit()

        
        #Tabla imagen-predio
        archivo_imagen = request.files['imagen_predio']
        if archivo_imagen.filename:
            
            imagen_data = archivo_imagen.read()

            new_imagenes_predio = Imagenes_predio(id_predio, nombre, imagen_data)

            db.session.add(new_imagenes_predio)
            db.session.commit()

        #Tabla Solicitud
        id_cliente = 1
        fecha = datetime.now()
        estado = 1
        descripcion = "Nueva solicitud: " + nombre

        new_solicitud = Solicitud(id_cliente, id_predio, fecha, estado, descripcion)

        db.session.add(new_solicitud)
        db.session.commit()

    
    flash('¡Su solicitud ha sido enviada! en 48 horas como máximo recibirá una respuesta')

    return redirect(url_for('conexion.reservar', id_predio = id_predio, id_image = new_imagenes_predio.id_image))
    
@conexion.route("/reservar/<string:id_predio>%<string:id_image>", methods=["GET"])
def reservar(id_predio, id_image):
    
    predio = Predio.query.get(id_predio)
    imagenes_predio = Imagenes_predio.query.get(id_image)
    tipo_predio = Tipo_predio.query.get(predio.id_tipo)

    predio_seguridad = Predio_seguridad.query.filter_by(id_predio=predio.id_predio).all()

    predios_areas_comunes = Predio_area_comun.query.filter_by(id_predio = predio.id_predio).all()

    seg_interna = ""
    seg_externa = ""

    areas_comunes = []

    for i in range(len(predio_seguridad)):
        s = Seguridad.query.get(predio_seguridad[i].id_seguridad)

        if s.tipo_seguridad == 1:
            seg_interna += "- "+s.nombre_seguridad + "\n"
        else:
            seg_externa += "- "+s.nombre_seguridad + "\n"

    for j in range(len(predios_areas_comunes)):
        area = Area_comun.query.get(predios_areas_comunes[j].id_area)
        areas_comunes.append({'tipo':area.tipo, 'area':predios_areas_comunes[j].area})

    C = 15000

    cotizacion = (predio.area*0.4 + predio.nro_casas_habitacion*0.2 + predio.nro_puertas_acceso*0.05 + predio.nro_torres_bloques*0.2 + len(predios_areas_comunes)*0.1 + len(predio_seguridad)*0.05)*C

    imagen_data = imagenes_predio.imagen

    imagen_url = f"data:image/jpeg;base64,{base64.b64encode(imagen_data).decode()}"
    

    return render_template("realizarSolicitud.html", predio = predio, cotizacion = cotizacion,
                           imagen_url = imagen_url, tipo_predio = tipo_predio, seg_interna = seg_interna,
                            seg_externa = seg_externa, areas_comunes = areas_comunes)

@conexion.route('/nuevaSolicitud/<string:id_predio>/<string:id_cliente>', methods=['POST'])
def add_solicitud(id_predio, id_cliente):
    if request.method == 'POST':

        id_cliente = id_cliente
        id_predio = id_predio
        fecha = datetime.now()
        estado = False

        new_solicitud = Solicitud(id_cliente, id_predio, fecha, estado)

        db.session.add(new_solicitud)
        db.session.commit()

        flash('Solicitud registrada correctamente')

        return redirect(url_for('conexion.index'))
