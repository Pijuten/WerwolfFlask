import binascii
import os
from flask import jsonify

import utils


def host(request):
    if testIfGreaterNull(int(request["werwolf"])):
        return jsonify({'success': 'error no werwolfs selected'})
    return jsonify({'success': 'ok', 'token': utils.generate_key()})


def testIfGreaterNull(intNumb):
    if intNumb <= 0:
        return False

