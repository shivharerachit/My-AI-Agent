from flask import Flask, Blueprint, Response, request, jsonify, make_response
from flask_restx import Api, Resource, fields, reqparse
from core_apis.payloads import *

import json


from core_apis.control import *




api = Api()


chatgpt = Blueprint('chatgpt', __name__, url_prefix='/chatgpt')
chatgpt_api = Api(chatgpt, version="1.0", title="chatgpt", description="Chatgpt Virtual Code Assistant")
chatgpts = chatgpt_api.namespace('chatgpt', description='Chatgpt Virtual Code Assistant')

nested_model = api.model('NestedModel', {
    'nested_field': fields.String(description='Nested Field'),
})
main_model = api.model('MainModel', {
    'field1':  fields.String(description='Field 1'),
    'nested': fields.Nested(nested_model),
})


@chatgpts.route('/server_test')
class ServerTest(Resource):
    @api.expect(server_test, validate=True)
    def get(self):
        try:
            args = server_test.parse_args()
            val = args['arg']
            print(val)
            return 'server running', 200
        except Exception as e:
            print('Error in server test : ', e)
            return f'Error occured in my route : {e}', 500


@chatgpts.route('/ask')
class GPT(Resource):
    # @api.expect(ttm_friend, validate=True)
    def post(self):
        try:
            prompt = request.get_json()
            print(prompt)
            code = prompt['code']
            print("code = \n\n\n\n", code, "\n\n\n\n")
            return askGPT(code)
        except Exception as e:
            print('Error in GPT : ', e)
            return f'Error occured in my GPT : {e}', 500        