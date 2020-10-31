from flask import Flask
from prometheus_exporter import gen_prometheus_out
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bayern Corona cases Prometheus exporter"

@app.route("/metrics")
def prom_export():
    return gen_prometheus_out()

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)