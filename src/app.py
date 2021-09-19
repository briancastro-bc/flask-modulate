from flask.app import Flask
from src.routes import routes
from src.database import db

class Application:
    
    app: Flask
    
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.settings()
        self.__register_routes()
        self.__register_error_handlers()
        self.__init_db()
    
    def start(self) -> None:
        try:
            self.app.run(self.app.config['HOST'], self.app.config['PORT'], self.app.config['DEBUG'], load_dotenv=True)
        except Exception as e:
            print("Error: {0}".format(e))
    
    def settings(self) -> None:
        try:
            self.app.config.from_pyfile('../appconfig.cfg')
            self.app.config.from_pyfile('../.env')
            self.app.config.from_mapping(
                SECRET_KEY=self.app.config['SECRET_KEY']
            )
            self.app.config['SQLALCHEMY_DATABASE_URI'] = self.app.config['DATABASE_CONN']
            db.init_app(self.app)
        except KeyError as e:
            print("Ocurrió un error con la variable de entorno. Key error: {0}".format(e))
        except Exception as e:
            print("Error: {0}".format(e))
    
    def __register_routes(self) -> None:
        self.app.add_url_rule(routes['index'], view_func=routes['index_controller'])
        self.app.add_url_rule(routes['login'], view_func=routes['login_controller'])
        self.app.add_url_rule(routes['signup'], view_func=routes['signup_controller'])
    
    def __register_blueprints(self) -> None:
        #self.app.register_blueprint(routes['blueprint'], url_prefix="/blueprint")
        pass
    
    def __register_error_handlers(self) -> None:
        pass
    
    def __init_db(self) -> None:
        db.create_all(app=self.app)