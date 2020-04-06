from flask import request # microframework , se declara flask
from flask import Flask 
import json
from datetime import datetime


app = Flask(__name__) # arranca


@app.route('/register/data', methods=['GET', 'POST']) # se declara una ruta para la aplicación API, que maneja GET y POST
def register_data():
    error = None # error vacio
    if request.method == 'POST': # si es post se hace lo siguiente
        today = datetime.now() # se define hoy
        filename = './files/' + request.form['ip'] + '_' + today.strftime("%Y-%m-%d-%H-%M-%S") # dentro de la carpeta files, tome la IP, y transforme en la fecha
        _data = {
            'hostname': request.form['hostname'], # hostname
            'ip': request.form['ip'], # IP
            'porc_disp': request.form['disk_usage'], # % de disco disponible
            'cpu_usage': request.form['cpu_usage'], # CPU
            'ram_usage': request.form['ram_usage'], # RAM
            'users': request.form['users'], # Usuarios
            'process' : json.loads(request.form['process']) # Procesos leidos como JSON
        }


        create_file(filename, _data) 
        return "created"



def create_file(filename, json_data): # Crea los archivos
    extension = '.json' # se lee Json
    with open(filename+extension, 'w') as file: # variable, nombre de archivo y ubicación
        json.dump(json_data, file, indent=4) # se consigue el archivo que queda en la carpeta files
        
