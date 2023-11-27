from flask import Flask
from kafka import KafkaConsumer, KafkaProducer

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