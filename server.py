from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from auth import auth as auth_blueprint
from api import api as api_blueprint
from main import main as main_blueprint
from model.authenticated_user import AuthenticatedUser

from service import user_service

app = Flask(__name__, static_url_path='', static_folder='static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'a0058c76-d45b-4c01-8881-8efacb2e9a9a'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user_details = user_service.get_user_by_id(int(user_id))
    return AuthenticatedUser(user_details)


app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
