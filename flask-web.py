from flask import Flask, request, render_template, Response
from kafka import KafkaConsumer, KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER, #KAFKA SERVER
    # security_protocol="SSL", 
    # ssl_cafile=CERTS_FOLDER + "/ca.pem",
    # ssl_certfile=CERTS_FOLDER + "/service.cert",
    # ssl_keyfile=CERTS_FOLDER + "/service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def stream_template(template_name, **context):
    """Enabling streaming back results to app"""
    app.update_template_context(context)
    template = app.jinja_env.get_template(template_name)
    streaming = template.stream(context)
    return streaming

@app.route('/send-rdy-message/<my_id>', methods=['POST'])
def pizza_ready(my_id=None):
    """Endpoint to pass ready pizzas"""
    print(my_id)
    producer.send(
        TOPIC_DELIVERY_NAME,
        key={"timestamp": my_id},
        value=request.json
    )
    producer.flush()
    return "OK"


if __name__ == "__main__":
    app.run(debug=True, port=5000)