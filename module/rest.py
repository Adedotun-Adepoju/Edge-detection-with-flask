from module import api,db
from module.models import img_schema, imgs_schema, Image
from flask import request,jsonify
from flask_restful import Resource

class GetName(Resource):
    def get(self):
        file_names = Image.query.all()
        results = imgs_schema.dump(file_names)
        return jsonify(results)

    def post(self):
        img_name = request.json["img_name"]
        new_file = Image(img_name)
        db.session.add(new_file)
        db.session.commit()

        return img_schema.jsonify(new_file)

class spec_id(Resource):
    def put(self,id):
        file = Image.query.get(id)

        file_name = request.json['img_name']
        file.img_name = file_name

        db.session.commit()

        return img_schema.jsonify(file)

    def get(self, id):
        file = Image.query.get(id)
        return img_schema.jsonify(file)

    def delete(self, id):
        file = Image.query.get(id)
        db.session.delete(file)
        db.session.commit()

api.add_resource(GetName,"/image")
api.add_resource(spec_id, "/image/<int:id>")