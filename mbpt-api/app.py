from flask import Flask
from routes.billers import billers_bp

app = Flask(__name__)

# Register the Blueprints
app.register_blueprint(billers_bp)

if __name__ == '__main__':
    app.run(debug=True)
