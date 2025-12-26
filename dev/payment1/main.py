import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

@app.route('/payment/<int:amount>', methods=['GET'])
def payment(amount):
    if amount != 0:
        logger.info("success0")
        return jsonify({"msg": "success2"}), 200
    logger.error("fail0")
    return jsonify({"msg": "fail2"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)