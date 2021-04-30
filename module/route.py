import os
import cv2
from module import app, det_edge
from flask import render_template, redirect, url_for, request, send_from_directory,flash
from module.forms import ImageForm
from werkzeug.utils import secure_filename



@app.route("/", methods=["GET","POST"])
def upload_image():
    form=ImageForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            img = form.image.data

            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            img_edges = det_edge(full_filename)
            cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'],filename), img_edges)
            return render_template("detect.html", filename=filename)

    return render_template("home.html",form=form)


