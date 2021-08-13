from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

Data=[]

class People(Resource):
    def get(self):
        for x in Data:
            if x['Data']==__name__:
                return x
        return {'Data':None}


    def post(self, name):
        Tem = {'Data':name}
        Data.append(Tem)
        return Tem

    def delete(self):
        for ind,x in enumerate(Data):
            if x['Data']==__name__:
                Tem = Data.pop(ind)
                return {'None':"Deleted"}

api.add_resource(People,'/Name/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)