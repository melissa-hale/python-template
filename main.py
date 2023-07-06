from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/flaskAPI/v1/properties')
def index():
    propertyList = [{
        "address": "123 Main",
        "bedrooms": 3,
        "bathrooms": 1
    }, {
        "address": "456 Walnut",
        "bedrooms": 2,
        "bathrooms": 2
    },
    {
        "address": "901 Walnut",
        "bedrooms": 3,
        "bathrooms": 2
    }]
    return jsonify(propertyList)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
