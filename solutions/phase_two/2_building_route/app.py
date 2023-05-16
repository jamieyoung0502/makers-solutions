import os
from flask import Flask, request

# creates an instance of the Flask class and passes __name__ as an argument.
# This tells Flask the name of the current module, which is necessary for Flask to determine the root path of the application.
# It helps Flask locate resources such as templates and static files relative to the module.
# When a Python file is run directly its __name__ variable is set to the string '__main__'
app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    message = request.form['message']

    # Send back a fond farewell with the name
    return f"Thanks {name}, you sent this message: \"{message}\""

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"

# from example_routes import apply_example_routes
# apply_example_routes(app)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

# This conditional statement checks if the current script is being executed as the main script
# If the script is being executed as the main script, this line starts the Flask development server and runs the application
# app.run(...), is only executed when the file is executed directly, not when it is imported as a module