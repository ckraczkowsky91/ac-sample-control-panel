# Configure the bootstrapped template to use
FLASK_ADMIN_SWATCH = 'paper'
# Configure the URI for the database
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/sample-flask-app-with-postgresql'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'secretkey'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = 'none'
SECURITY_SEND_REGISTER_EMAIL = False
# Configure Flask-Security to go to Flask-Admin index view after login view
SECURITY_POST_LOGIN_VIEW = '/admin/'
# Configure Flask-Security to go to Flask-Admin index view after logout view
SECURITY_POST_LOGOUT_VIEW = '/admin/'
# Configure Flask-Security to go to Flask-Admin index view after register view
SECURITY_POST_REGISTER_VIEW = '/admin/'
