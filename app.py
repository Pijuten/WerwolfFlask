from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from services import HostService

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/host', methods=['POST'])
@cross_origin(supports_credentials=True)
def host():
    if request.method == 'POST':
        rolesData = request.json
        print(rolesData)
        return HostService.host(rolesData);
    else:
        return jsonify({'success': 'error'})


if __name__ == '__main__':
    app.run(debug=True)
