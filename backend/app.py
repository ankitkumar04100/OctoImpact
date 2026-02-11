from flask import Flask
from flask_cors import CORS
from config import Config
from dashboard_routes import dashboard_bp
from rewards_routes import rewards_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(dashboard_bp)
app.register_blueprint(rewards_bp)

@app.route("/")
def home():
    return "<h1>Welcome to OctoImpact Backend!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
