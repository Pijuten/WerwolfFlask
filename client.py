import requests
import json


ip="http://127.0.0.1:5000"


def get():
    response=requests.get(ip)
    print(response.json())

def send(msg):
    response=requests.post(ip,{'data':msg})
    print(response.json())



def host(name,settings='{"werwolf":1,"hexe":1,"gerber":1}'):
    msg='{"action":"host", "settings":'+settings+',"name":"'+name+'"}'
    response=requests.post(ip,{'data':msg}).json()
    if response["status"]=="success":
        print(f"Success! Lobby ID:{response['lobbyID']}")
        player=Game(name,response["playerID"],response["lobbyID"],settings,True)
        player.players.append(name)
        return player
    else:
        print(response["status"])

def join(name,lobbyID):
    msg='{"action":"connect", "lobbyID":'+str(lobbyID)+',"name":"'+name+'"}'
    response=requests.post(ip,{'data':msg}).json()
    if response["status"]=="success":
        print(f"Success!")
        player=Game(name,response["playerID"],lobbyID,response["lobbySettings"],False)
        player.players=response["players"]
        return player
    else:
        print(response["status"])

def wait(player):
    msg='{"action":"waiting"}'
    #, "lobbyID":'+str(player.lobbyID)+'
    response=requests.post(ip,{'data':msg}).json()

class Game:
    def __init__(self,name,playerID,lobbyID,settings,isHost):
        self.lobbyID=lobbyID
        self.playerID=playerID
        self.players=[]
        self.name=name
        self.inGame=False
        self.settings=settings
        self.isHost=isHost
        
    def printSelf(self):
        print("LobbyID: ",self.lobbyID)
        print("playerID: ",self.playerID)
        print("players: ",self.players)
        print("name: ",self.name)
        print("inGame: ",self.inGame)
        print("settings: ",self.settings)
        print("isHost: ",self.isHost)
