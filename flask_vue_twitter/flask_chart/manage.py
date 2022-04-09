# 导入script扩展
from flask_cors import CORS
from flask_script import Manager
# 导入migrate扩展
from flask_migrate import Migrate,MigrateCommand

from info import create_app,db,models

app = create_app('development')
CORS(app, supports_credentials=False)

manage = Manager(app)
Migrate(app,db)
manage.add_command('db',MigrateCommand)

"""
migrate step:
python manage.py db init
python manage.py db migrate -m 'init_tables'
python manage.py db upgrade

"""

if __name__ == '__main__':
    # app.run(debug=True)
    # print(app.url_map)
    manage.run()