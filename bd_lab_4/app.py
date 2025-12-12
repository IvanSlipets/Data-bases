from flask import Flask
from ruamel.yaml import YAML
import os
import sys


project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project')
if project_root not in sys.path:
    sys.path.append(project_root)


from project.my_project.auth.route.athlete_route import athlete_bp
from project.my_project.auth.route.sport_route import sport_bp
from project.my_project.auth.route.competition_route import competition_bp
from project.my_project.utils.db_init import db

def create_app():
    app = Flask(__name__)
    
    yaml = YAML()
    config_path = os.path.join(app.root_path, 'project', 'config', 'app.yml')

    print(f"Attempting to load config from: {config_path}")
    
    with open(config_path, 'r') as f:
        config = yaml.load(f)

    app.config['SECRET_KEY'] = config['app']['secret_key']
    app.config['DEBUG'] = config['app']['debug']
    
    db_config = config['database']
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(athlete_bp, url_prefix='/api/athletes')
    app.register_blueprint(sport_bp, url_prefix='/api/sports')
    app.register_blueprint(competition_bp, url_prefix='/api/competitions')

    return app

if __name__ == '__main__':
    app = create_app()
    # Створення таблиць у базі даних, якщо вони ще не існують
    with app.app_context():
        pass
    app.run(host='0.0.0.0', port=5000)