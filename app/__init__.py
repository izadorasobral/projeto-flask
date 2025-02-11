<<<<<<< HEAD
=======
import os
>>>>>>> 219be471f3877456075f0426714630602e9b156c
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

<<<<<<< HEAD
# Inicialize extensões
=======
>>>>>>> 219be471f3877456075f0426714630602e9b156c
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    # Inicialize extensões com a aplicação
    db.init_app(app)
    login_manager.init_app(app)
    
    # Importar e registrar o blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))
=======
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')

    # Certifique-se de que o diretório da instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
>>>>>>> 219be471f3877456075f0426714630602e9b156c
