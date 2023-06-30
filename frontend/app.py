from flask import Flask, render_template, request
from backend_consumer import PrClient


app = Flask(__name__)
pr_client  = PrClient()


@app.route('/')
def start():

    return render_template('index.html')

@app.route('/product', methods=[ 'POST', 'GET'])
def product():

    product = request.values.get('product')

    product = pr_client.process_get(f'price?product={product}')

    return render_template('index.html', product=product.json())


if __name__== "__main__":
    app.run(host='0.0.0.0', debug = True, port = 5004)

