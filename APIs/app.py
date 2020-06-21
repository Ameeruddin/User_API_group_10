from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.teamregister import Register,Teamstatus,Sportdetails,Reporttimes,Sportcategory,Schedules

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='group10'
app.config['PREFERRED_URL_SCHEME']='http'
api=Api(app)
jwt=JWTManager(app)
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401


api.add_resource(Register,'/register')
api.add_resource(Teamstatus,'/teamstatus')
api.add_resource(Sportdetails,'/sportdetails')
api.add_resource(Reporttimes,'/reporttime')
api.add_resource(Sportcategory,'/sportcategory')
api.add_resource(Schedules,'/schedules')
if __name__ == "__main__":
    app.run(port="8055",debug=True)
