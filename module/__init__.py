import os
import cv2
from flask import Flask

app = Flask(__name__, static_folder='C:/Users/USER/Desktop/iQube/projects/week 4/edge_detection/static/images')
UPLOAD_FOLDER = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='a58d2762c5d24aee56d3621b'

print(UPLOAD_FOLDER)


def det_edge(img):
    img_array = cv2.imread(img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

    return img_edges

from module import route
