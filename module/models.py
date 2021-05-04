from module import db
from module import ma

class Image(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    img_name = db.Column(db.String(1024), unique = False)

    def __init__(self, img_name):
        self.img_name = img_name

class ImgSchema(ma.Schema):
    class Meta:
        fields = ('id','img_name')

# Init schema
img_schema = ImgSchema()
imgs_schema = ImgSchema(many=True)
