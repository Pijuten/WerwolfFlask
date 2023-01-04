from flask import jsonify


def host(request):
    return jsonify({'success': 'ok'})
