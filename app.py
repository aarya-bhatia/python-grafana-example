import random
import time
from flask import Flask
from prometheus_client import Counter, Summary, generate_latest

app = Flask(__name__)

view_metric = Counter('view', 'Product view', ['product'])
buy_metric = Counter('buy', 'Product buy', ['product'])
duration = Summary('duration_compute_seconds',
                   'Time spent in the compute() functionk')
exception = Counter('compute_exception',
                    'Exception thrown in compute() function')


@exception.count_exceptions()
def compute():
    if random.uniform(0, 10) > 7:
        raise Exception("Random error")


@duration.time()
def compute():
    time.sleep(random.uniform(0, 10))


@app.route('/view/<id>')
def view_product(id):
    view_metric.labels(product=id).inc()
    return "View %s" % id


@app.route('/buy/<id>')
def buy_product(id):
    buy_metric.labels(product=id).inc()
    return "Buy %s" % id


@app.route('/metrics')
def metrics():
    return generate_latest()
