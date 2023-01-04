from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import time
import random
import json

app=Flask(__name__)
api=Api(app)


class Game:
    def __init__(self,settings):
        self.id=random.randint(1000,9999)
        self.players=[]
        self.inGame=False
        self.settings=settings

    #macht das Game object zu einem JSON, und auch alle Children, also das players array mit den Player classes werden auch JSON, code von chatGPT
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
         
class Player:
    def __init__(self,name):
        self.name=name
        self.id=random.randint(0,1000000000)

class HelloWorld(Resource):
    def get(self):
        global game
        return game.to_json()
    
    def post(self):
        global game
        form=json.loads(request.form['data'])
        match form["action"]:
            case "host":
                print("----------Host request----------")
                error=checkSettings(form["settings"])
                if not error:
                    print("----------Creating Lobby----------")
                    game=Game(form["settings"])
                    player=Player(form["name"])
                    game.players.append(player)
                    return {"status":"success",
                            "lobbyID":game.id,
                            "playerID":player.id}
                else:
                    print(f"----------Error: {error}----------")
                    return {"status":error}
            case "connect":
                print(f"----------Connecting...----------")
                if form["lobbyID"]!=game.id:
                    print(f"----------Lobby ID not found----------")
                    return {"status":"Lobby ID not found"}
                if form["name"] in [x.name for x in game.players]:
                    print(f"----------Name Taken----------")
                    return {"status":"Name Taken"}
                player=Player(form["name"])
                game.players.append(player)
                print(f"----------Success----------")
                players=[x.name for x in game.players]
                return {"status":"success",
                        "playerID":player.id,
                        "players":players,
                        "lobbySettings":game.settings}
            case "waiting":
                while True:
                    time.sleep(1)
                return
            case "inGameAcion":
                return

def checkSettings(settings):
    if settings["werwolf"]>5:
        return "Zu viele Wölfe"
    elif settings["gerber"]!=1:
        return "Kein Gerber"
    else:
        return False
    
    

api.add_resource(HelloWorld,"/")

if __name__=="__main__":
    app.run(debug=True)
