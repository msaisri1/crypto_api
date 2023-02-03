from flask_marshmallow import Marshmallow,fields


ma = Marshmallow()



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)