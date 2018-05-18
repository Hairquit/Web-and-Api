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


@api.route('/')
class SaloonList(Resource):
    @api.doc('list_saloons')
    @api.marshal_list_with(saloon)
    def get(self):
        '''List all saloons'''
        SALOONS = Saloon.query.all()
        return SALOONS

    @api.doc('create_saloon')
    @api.expect(saloon)
    def post(self):
        print(" request input is " + str(request.get_json()))
        try:
            inputSaloon = Saloon();
            inputSaloon.create(request.get_json())
            alchemydb.session.add(inputSaloon)
            alchemydb.session.commit()
        except Exception as e:
            print( "Exception throw {}" .format(e) );
        return "Your information was saved successfully" ,200


@api.route('/<name>')
@api.param('name', 'The saloon identifier')
@api.response(404, 'Saloon not found')
class SaloonUnit(Resource):
    @api.doc('get_saloon')
    @api.marshal_with(saloon)
    def get(self, name):
        '''Fetch a saloon given its identifier'''
        saloon = Saloon.query.filter(Saloon.saloonName == name).one()
        return saloon
        api.abort(404)
