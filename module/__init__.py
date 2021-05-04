import os
import cv2
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

UPLOAD_FOLDER = os.path.join(os.getcwd(),'static/images')
BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder=UPLOAD_FOLDER)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='a58d2762c5d24aee56d3621b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

def det_edge(img):
    img_array = cv2.imread(img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

    return img_edges



from module import route
from module import rest
