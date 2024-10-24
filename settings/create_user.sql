-- Crear un nuevo usuario con una contraseña segura
CREATE USER 'flask_user_name'@'localhost' IDENTIFIED BY 'flask_user_password';

-- Conceder todos los privilegios en la base de datos 
GRANT ALL PRIVILEGES ON flask_app_db.* TO 'flask_user_name'@'%' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios (no es obligatorio en versiones modernas de MySQL)
-- FLUSH PRIVILEGES;

-- Verificar los privilegios del nuevo usuario
SHOW GRANTS FOR 'flask_user_name'@'localhost';