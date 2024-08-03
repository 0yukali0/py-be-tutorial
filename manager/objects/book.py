from marshmallow import Schema, fields

class Arthor:
    def __init__(self, name: str):
        self.name = name

class ArthorSchema(Schema):
    name = fields.String()

class Book:
    def __init__(self, name: str, price: int, arthor: Arthor):
        self.name = name
        self.price = price
        self.arthor = arthor

class BookSchema(Schema):
    name = fields.String()
    price = fields.Integer()
    arthor = fields.Nested(ArthorSchema)