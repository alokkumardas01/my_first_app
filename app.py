from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    ## Run the app when this script is executed
    app.run()
