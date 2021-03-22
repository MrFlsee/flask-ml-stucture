from flask import Flask
from flask_restx import Resource, Api, Namespace

Interface = Namespace(
    name='interface',
    description='open Apis'
)

@Interface.route('generate')
class GenerateRule(Resource):
    def post(self):
        """
        Rule을 생성한다. 
        """
        pass

@Interface.route('request')
class RequestFirewallAnalysis(Resource):
    def post(self):
        """
        방화벽 분석을 요청한다.
        """
        pass

@Interface.route('status')
class GetAnalysisStatus(Resource):
    def get(self):
        """
        분석 현황을 조회한다.
        """
        pass

@Interface.route('rulesimilar')
class GetSimilarRule(Resource):
    def get(self):
        """
        유사 정책을 찾는다.
        """
        pass

@Interface.route('firewallinfo')
class GetFirewallInformation(Resource):
        def get(self):
        """
        방화벽 전체의 정보를 요청한다.
        방화벽의 룰 편중성, 통계 정보등을 리턴한다.
        """
        pass

@Interface.route('firewallvisual')
class GetVisualFirewallInformation(Resource):
    """
    방화벽 정책의 visualization 정보를 요청한다.
    key : value(base64)
    """
    pass

@Interface.route('ruleinfo')
class GetRuleInformation(Resource):
    """
    특정 정책에 대한 정보를 요청한다.
    """
    pass

@Interface.route('rulevisual')
class GetVisualRuleInformation(Resource):
    """
    특정 정책에 대한 visualization 정보를 요청한다.
    key : value(base64)
    """
    pass



#@api.route('')
#class TodoPost(Resource):
#    def post(self):
#        global count
#        global todos
#
#        idx = count
#        count += 1
#        todos[idx] = request.json.get('data')
#
#        return {
#            'todo_id': idx,
#            'data': todos[idx]
#        }
#
#@api.route('/<int:todo_id>')
#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {
#            'todo_id': todo_id,
#            'data': todos[todo_id]
#        }
#
#    def put(self, todo_id):
#        todos[todo_id] = request.json.get('data')
#        return {
#            'todo_id': todo_id,
#            'data': todos[todo_id]
#        }
#
#    def delete(self, todo_id):
#        del todos[todo_id]
#        return {
#            'delete': 'success'
#        }


