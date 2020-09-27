import logging
import json
from svglib.svglib import svg2rlg

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])
def evaluateBucket():
    # data = request.get_json();
    # logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = { "result" : 1130 }
    logging.info("My result :{}".format(result))
    return json.dumps(result);

