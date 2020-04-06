from flask import request 
from flask import Flask 
import json
from datetime import datetime


app = Flask(__name__) 


@app.route('/register/data', methods=['GET', 'POST']) 
def register_data():
    error = None 
    if request.method == 'POST': 
        today = datetime.now() 
        filename = './files/' + request.form['ip'] + '_' + today.strftime("%Y-%m-%d-%H-%M-%S") 
        _data = {
            'hostname': request.form['hostname'], 
            'ip': request.form['ip'], 
            'porc_disp': request.form['disk_usage'], 
            'cpu_usage': request.form['cpu_usage'], 
            'ram_usage': request.form['ram_usage'], 
            'users': request.form['users'], 
            'process' : json.loads(request.form['process']) 
        }


        create_file(filename, _data) 
        return "created"



def create_file(filename, json_data): 
    extension = '.json' 
    with open(filename+extension, 'w') as file: 
        json.dump(json_data, file, indent=4) 
        
