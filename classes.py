from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

class GreetingAPI(MethodView):
    def get(self):
        # Handles GET requests
        return jsonify({"message": "Welcome to Flask in a feature branch!"})

    def post(self):
        # Handles POST requests
        data = request.get_json()
        name = data.get('name', 'Guest')
        return jsonify({"message": f"Hello, {name}!"})

# Register the class-based view
app.add_url_rule('/', view_func=GreetingAPI.as_view('greeting_api'))

if __name__ == '__main__':
    app.run(debug=True)

