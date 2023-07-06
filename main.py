from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)
api = Api(app, '/thisapi')

# Configure swagger
SWAGGER_URL = '/thisapi/docs'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'teamplate API'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

# define health check
class HealthCheck(Resource):
    def get(self):
        return jsonify({"message": "All systems go."})
# add endpoint to API
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
