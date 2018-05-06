from flask_restplus import Namespace, Resource, fields

api = Namespace('saloons', description='Saloons related operations')

saloon = api.model('Saloon', {
    'id': fields.String(required=True, description='The saloon identifier'),
    'name': fields.String(required=True, description='The saloon name'),
})

SALOONS = [
    {'id': 'felix', 'name': 'Felix'},
    {'id': 'saloonista', 'name': 'saloonista'},
    
]

@api.route('/')
class SaloonList(Resource):
    @api.doc('list_saloons')
    @api.marshal_list_with(saloon)
    def get(self):
        '''List all saloons'''
        return SALOONS

@api.route('/<id>')
@api.param('id', 'The saloon identifier')
@api.response(404, 'Saloon not found')
class Saloon(Resource):
    @api.doc('get_saloon')
    @api.marshal_with(saloon)
    def get(self, id):
        '''Fetch a saloon given its identifier'''
        for saloon in SALOONS:
            if saloon['id'] == id:
                return saloon
        api.abort(404)