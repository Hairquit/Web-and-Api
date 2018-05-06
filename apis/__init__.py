from flask_restplus import Api
from .saloon import api as ns1

api = Api(
    title='Hair cut',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1, path='/haircut')
