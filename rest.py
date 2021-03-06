from flask_restplus import Api
from flask.blueprints import Blueprint
from flask import request
from configVariable import logger

blueprint = Blueprint('api', __name__)
ml = Api(blueprint, doc='/swagger')

ml = ml.namespace('', description='MachineLearning Service')

@blueprint.before_request
def requestauth(*args, **kwargs):
    '''
    rest api에 해당하는 함수가 호출되기 전 수행되는 내용
    '''

    remoteaddr = ''

    if request.headers.getlist("X-Forwarded-For"):
        remoteaddr = request.headers.getlist("X-Forwarded-For")[0]
    else:
        remoteaddr = request.remote_addr

    logger.info('RESTService request. path=' + request.path + ', method=' + request.method + ', remote_addr=' + remoteaddr)
