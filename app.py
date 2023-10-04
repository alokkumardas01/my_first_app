from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Welcome to Render Cloud Platform.."

if __name__ == "__main__":
    ## Run the app when this script is executed
    app.run()
