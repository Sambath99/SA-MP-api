from flask import Flask, jsonify
from samp_py.client import SampClient

app = Flask(__name__)

@app.route('/<server_address>')
def get_server_info(server_address):
    ip, port = server_address.split(':')
    port = int(port)

    with SampClient(address=ip, port=port) as samp_client:
        server_info = samp_client.get_server_info()
        clients_detailed = samp_client.get_server_clients_detailed()

    formatted_data = {
        "server_info": server_info,
        "detailed_clients": [
            {
                "id": player.id,
                "name": player.name,
                "score": player.score,
                "ping": player.ping
            }
            for player in clients_detailed
        ]
    }

    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
