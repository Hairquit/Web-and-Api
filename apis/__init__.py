from flask_restplus import Api
from flask import Blueprint
from .saloon import api as ns1
from .users import api as ns2


api = Api(
    title='Hair cut',
    version='1.0',
    description='A description',
    # All API metadatas
)

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)


api.add_namespace(ns1, path='/providers')
api.add_namespace(ns2, path='/consumers')