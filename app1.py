from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/system_info', methods=['GET'])
def system_info():
    # Obtener información del sistema
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_info = psutil.net_io_counters(pernic=True)

    # Mostrar en la terminal que la API está siendo consumida
    print("Consumiendo API para obtener información del sistema...")

    # Mostrar información del sistema en la terminal
    print(f"Uso de CPU: {cpu_percent}%")
    print(f"Uso de RAM: {ram_percent}%")
    print(f"Uso de disco: {disk_percent}%")
    print(f"Información de red: {network_info}")

    # Retornar la información del sistema como JSON
    system_info = {
        'cpu_usage_percent': cpu_percent,
        'ram_usage_percent': ram_percent,
        'disk_usage_percent': disk_percent,
        'network_info': network_info
    }
    return jsonify(system_info)

if __name__ == '__main__':
    app.run(debug=True)
