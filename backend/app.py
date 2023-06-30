from flask import Flask, render_template, request

app = Flask(__name__)

products = {

    "iphone": {
        "name": "iPhone X",
        "price": 1000,
    },
    "samsung": {
        "name": "Samsung S10",
        "price": 800,
    },
    "huawei": {
        "name": "Huawei P30",
        "price": 588,
    },
    "xiaomi": {
        "name": "Xiaomi Redmi Note 8",
        "price": 699,
    },
    "oppo": {
        "name": "Oppo Reno2",
        "price": 784,
    },
    "vivo": {
        "name": "Vivo V19",
        "price": 458,
    },
    "nokia": {
        "name": "Nokia 6.1",
        "price": 782,
    },
    "realme": {
        "name": "Realme 5",
        "price": 697,
    }
}

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result

@app.route('/price', methods=['GET', 'POST'])
def price():

    print ("here")

    product = request.values.get('product')

    if product in products:
        return products[product]
    else:
        return {"error": "product not found"}

    


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)