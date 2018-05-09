from flask_restplus import Namespace, Resource, fields
from database import mysql , alchemydb ,Saloon
from flask import json, request

api = Namespace('saloons', description='Saloons related operations')

saloon = api.model('saloon', {
    'saloonName' : fields.String(required=True, description='The saloon name'),
    'saloonAddress' : fields.String(required=True, description='The saloon address'),
    'capacity' : fields.String(required=False, description='The saloon capacity'),
    'customerCnt' : fields.String(required=False, description='The saloon customer count at this time '),
    'waitTime' : fields.String(required=False, description='The saloon expected wait time')
})

SALOONS = [
    {'saloonName': 'felix', 'saloonAddress': 'Felix'},
    {'saloonName': 'saloonista', 'saloonAddress': 'saloonista'},
    
]
       

@api.route('/')
class SaloonList(Resource):
    @api.doc('list_saloons')
    @api.marshal_list_with(saloon)
    def get(self):
        '''List all saloons'''
        return SALOONS

    @api.doc('create_saloon')
    @api.expect(saloon)
    def post(self):
        print(" request input is " +  str(request.get_json()))
        # saloon1 = Saloon( saloonName='hairisrocacy', saloonAddress='1 hair saloon way ')
        # alchemydb.session.add()
        # alchemydb.session.commit()
        return "hellow world" ,200


@api.route('/<id>')
@api.param('id', 'The saloon identifier')
@api.response(404, 'Saloon not found')
class SaloonUnit(Resource):
    @api.doc('get_saloon')
    @api.marshal_with(saloon)
    def get(self, id):
        '''Fetch a saloon given its identifier'''
        for saloon in SALOONS:
            if saloon['id'] == id:
                return saloon
        api.abort(404)