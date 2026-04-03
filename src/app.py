from flask import Flask, abort, jsonify
import logging
import sys

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handler to stdout
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(handler)

logger.info("Starting Flask application")

# Initialize Flask
healthy = True
app = Flask(__name__)

# Send Hello World
@app.route("/")
def hello_world():
    logger.info("Sending Hello world message")
    return jsonify({'message': 'Hello World!'})

# Return healthcheck Response
@app.route("/health")
def healthcheck():
    global healthy
    if healthy:
        logger.info("Application healthcheck successful")
        return jsonify({'status':'Application healthcheck successful'}), 200
    else:
        logger.info("Application healthcheck failed")
        return jsonify({'status':'Application healthcheck failed'}), 503

# Toggle healthcheck    
@app.route("/toggle-health")
def toggle_health():
    global healthy
    healthy = not healthy
    logger.info(f'Application ealth set to {healthy}')
    return jsonify({'message': f'health set to {healthy}'}), 200