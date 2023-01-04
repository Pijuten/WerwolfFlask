from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import time
import random
import json

app=Flask(__name__)
api=Api(app)


class HelloWorld(Resource):
    def post(self):
        global loop
        loop=True
        form=request.form
        print("GRAD GKOMMEN ->>", form["status"])
        if form["status"]=="STOP":
            loop=False
        while loop:
            time.sleep(1)
        print("Fertig ->>", form["status"])
        return {"status":form["status"]}  
    

api.add_resource(HelloWorld,"/")

if __name__=="__main__":
    app.run(debug=True)
