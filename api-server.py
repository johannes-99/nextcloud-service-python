import nextcloudservice 
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class FileList(Resource):

    def get(self):
        filesinput = nextcloudservice.read_webdav_dir("")
        filesoutput = []  

        for file in filesinput:
            
            filesoutput.append( {
                'name' : file.name,
                'dir' : file.directory, #TODO: bugfix dir contains name 
                'isdir' : file.isdir
                }) 

        return {'filelist': filesoutput }

api.add_resource(FileList, '/filelist')
class HelloWorld(Resource):

    def get(self):
         return {'hello': "world 1" }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')