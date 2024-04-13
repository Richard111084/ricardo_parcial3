from flask import Flask, jsonify
app = Flask(_name_)
tasks = [
    {"id":1, "user":"omar", "active":True},
    {"id":2, "user":"leo", "active":False},
    {"id":3, "user":"luz", "active":True},
    {"id":4, "user":"alan", "active":False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if _name_ == '_main_':
    app.run(debug=True)
    import json

file_name = "data.json"

with open(file_name, "r") as data:
    datos = json.load(data)
    #print("\nIP: " + datos["ip"] + "\nSO: " + datos["so"] )
    print(datos["info"][0])
 import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if(response.status_code == 200):
    data = response.json()
    print("Solicitud exitosa")
    #print("Datos", data)
    print("ID: ", data['id'], "\nMensaje: ", data['body'])

else:
    print("Error en la solicitud", response.text)
{
    "ip": "192.168.122.1\n10.171.72.149",
    "so": "Linux",
    "version": "6.1.0-1027-oem",
    "info": [
        "a",
        "b",
        "c"
    ],
    "hostname": "matebookNeon",
    "cpu": "x86_64"
}
[4:42 p. m., 2/4/2024] Jose Sosa: import platform
import sys
import subprocess
import json

sistemaop = sys.platform
sistema = platform.system()
version = platform.release()
hostname = platform.node()
cpu = platform.processor()

if(sistema == "Windows"):
    local = subprocess.getoutput("""for /f "tokens=2 delims==[]" %a in ('ping -n 1 -4 "%computername%"') do echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

diccionario = {'ip':local,'so':sistema,'version':version,'hostname': hostname,'cpu': cpu}

dictionaryToJson = json.dumps(diccionario)
print(dictionaryToJson)
file=open("data.json", "w")
json.dump(diccionario, file, indent=4)
file.close()