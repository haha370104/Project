from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ab123456@115.28.206.58:3306/Project'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ttkl1231@localhost:3306/Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#test