from api import app
from flask_mysqldb import MySQL

# Configuración de la conexión a la base de datos
# Deben utilizarse los MISMOS valores asignados al 
# crear la base de datos y el usuario correspondiente

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask_user_name'
app.config['MYSQL_PASSWORD'] ='flask_user_password'
app.config['MYSQL_DB'] = 'flask_app_db'
app.config['MYSQL_PORT'] = 3306

# Algunas opciones de configuración para servidores que no soportan SSL
# (no necesario si se instalan las versiones de paquetes indicadas en requirements.txt)
#app.config['MYSQL_USE_SSL'] = False 
#app.config['MYSQL_INIT_COMMAND'] = 'SET SESSION ssl_mode=DISABLED;'
#app.config['MYSQL_SSL_DISABLED'] = True

# Se crea una instancia de MySQL, que debe ser importada en cada archivo que requiera 
# conexión a la base de datos
mysql = MySQL(app)

class DBError(Exception):
    pass