import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

@app.route('/identify/<username>', methods=['GET'])
def identify(username):
    if username.isalpha():
        logger.info("success0")
        return jsonify({"msg": "success1"}), 200
    logger.error("fail0")
    return jsonify({"msg": "fail1"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)