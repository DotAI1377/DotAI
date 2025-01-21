from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Application configuration can be set here
def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    # Configure app settings here, e.g., database URI, secret keys, etc.
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register blueprints or modules
    # Example:
    # from app.routes import main_routes
    # app.register_blueprint(main_routes)

    return app

__all__ = ['create_app', 'app']
