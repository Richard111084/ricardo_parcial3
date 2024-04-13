from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/system_info', methods=['GET'])
def system_info():
    # Obtener información del sistema
    system_info = {
        'cpu_usage_percent': psutil.cpu_percent(interval=1),
        'ram_usage_percent': psutil.virtual_memory().percent,
        'disk_usage_percent': psutil.disk_usage('/').percent,
        'network_info': psutil.net_io_counters(pernic=True)
    }
    return jsonify(system_info)

if __name__ == '__main__':
    app.run(debug=True)

