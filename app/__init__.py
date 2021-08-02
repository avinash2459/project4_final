from flask import Flask


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False, template_folder="templates")
    app.config.from_pyfile('config.py')

    with app.app_context():
        # Include our Routes
        from Routes import routes
        from Routes.Add import routes
        from Routes.Edit import routes
        from Routes.Delete import routes
        from Routes.ErrorHandling import routes
        return app
