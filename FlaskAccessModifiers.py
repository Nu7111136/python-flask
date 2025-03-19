from flask import Flask, jsonify

app = Flask(__name__)

class User:
#####Initilization#############################################
    def __init__(self, name, email, password):
        self.name = name  # Public attribute
        self._email = email  # Protected attribute
        self.__password = password  # Private attribute
######################################
##BODY####################################################
    def get_public_info(self):
        return {"name": self.name}  # Access public attribute

    def _get_protected_info(self):
        return {"email": self._email}  # Access protected attribute

    def __get_private_info(self):
        return {"password": self.__password}  # Access private attribute

    def get_all_info(self):
        return {
            "name": self.name,
            "email": self._email,
            "password": self.__password  # Private accessible within the class
        }
#################################################################

###MAIN##########################################
# Creating a User object
user = User("Nouman", "nouman@example.com", "securepass")

@app.route('/public')
def public():
    return jsonify(user.get_public_info())  # Public accessible

@app.route('/protected')
def protected():
    return jsonify(user._get_protected_info())  # Not recommended, but accessible

@app.route('/private')
def private():
    # Direct access to private attributes outside the class will fail
    try:
        return jsonify({"password": user.__password})
    except AttributeError:
        return jsonify({"error": "Cannot access private attribute"}), 403

@app.route('/all')
def all_info():
    return jsonify(user.get_all_info())  # Accessing private data inside the class

if __name__ == '__main__':
    app.run(debug=True)
###########################################