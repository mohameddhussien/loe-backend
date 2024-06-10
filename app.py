from flask import Flask, g
from flask_cors import CORS
from routes.user_routes import user_bp
from routes.event_routes import event_bp
from utils.config import Config
from models.db import Database
from utils.network import NetworkUtils

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Load configuration
app.config.from_object(Config)
Config.init_app(app)

@app.before_request
def before_request():
    if not hasattr(g, 'db'):
        g.db = Database(
            host=app.config['DB_HOST'],
            name=app.config['DB_NAME'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD']
        )
        g.db.connect()

@app.teardown_appcontext
def teardown_appcontext(exception):
    db: Database | None = getattr(g, 'db', None)
    if db is not None:
        db.disconnect()

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(event_bp)

if __name__ == "__main__":
    host_ip = NetworkUtils.get_ipv4_address()
    app.run(debug=True, host=host_ip, port=5000)