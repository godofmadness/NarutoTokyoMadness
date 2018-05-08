from PodSixNet.PodSixNet.Channel import Channel
from PodSixNet.PodSixNet.Server import Server
import uuid
from time import sleep

SERVER_PORT = 5071
SERVER_IP = "172.20.10.2"

# Create the channel to deal with our incoming requests from the client
# A new channel is created every time a client connects
class ClientChannel(Channel):
    # Create a function that will respond to a request to move a player
    def Network_move(self, data):
        # Fetch the data top help us identify which game needs to update
        gameID = data['roomId']
        player = data['playerId']
        x = data['x']
        y = data['y']
        time = data['time']

        print("GAMEID: "  + str(gameID) + " Moving " + str(data['direction']) + " of player: " + str(player)+ " time " + str(time))
        # Call the move function of the server to update this game
        self._server.movePlayer(x, y, "move", gameID, player, data['direction'], time)


    def Network_stop(self, data):
        # Fetch the data top help us identify which game needs to update
        gameID = data['roomId']
        player = data['playerId']
        x = data['x']
        y = data['y']
        time = data['time']


        # Call the move function of the server to update this game
        print("GAMEID: " + str(gameID) + " Stopping " + str(data['direction']) + " of player: " + str(player)+ " time " + str(time))
        self._server.movePlayer(x, y, "stop", gameID, player,  data['direction'], time)

    def Network_jump(self, data):
        # Fetch the data top help us identify which game needs to update
        gameID = data['roomId']
        player = data['playerId']
        x = data['x']
        y = data['y']
        time = data['time']

        # Call the move function of the server to update this game
        print("GAMEID: " + str(gameID) + " Jumping " + str(data['direction']) + " of player: " + str(player)+ " time " + str(time))
        self._server.movePlayer(x, y, "jump", gameID, player, data['direction'], time)


    def Network_basicAttack(self, data):
        # Fetch the data top help us identify which game needs to update
        gameID = data['roomId']
        player = data['playerId']
        x = data['x']
        y = data['y']
        time = data['time']

        # Call the move function of the server to update this game
        print("GAMEID: " + str(gameID) + " Attacking " + str(data['direction']) + " of player: " + str(player) + " time " + str(time))
        self._server.movePlayer(x, y, "basicAttack", gameID, player, data['direction'], time)


    def Network_specialMove1(self, data):
        gameID = data['roomId']
        player = data['playerId']
        x = data['x']
        y = data['y']
        time = data['time']

        print("GAMEID: " + str(gameID) + " Special move 1 " + str(data['direction']) + " of player: " + str(
            player) + " time " + str(time))

        self._server.movePlayer(x, y, "specialMove1", gameID, player, data['direction'], time)


# Create a new server for our game
class GameServer(Server):
    # Set the channel to deal with incoming requests
    channelClass = ClientChannel

    # Constructor to initialize the server objects
    def __init__(self, *args, **kwargs):

        # Call the super constructor
        Server.__init__(self, localaddr=(SERVER_IP, SERVER_PORT), *args, **kwargs)

        # Create the objects to hold our game ID and list of running games
        self.rooms = {}
        self.room = None
        # self.gameIndex = 0
        self.currentActiveRoomId = None


    # Function to deal with new connections
    def Connected(self, channel, addr):
        print(addr)
        print("New connection: {}".format(channel))

        player = Player(str(uuid.uuid4()), channel, 0, 0)

        # When we receive a new connection
        # Check whether there is a game waiting in the queue
        if self.room == None:
            print("Creating new room")
            # If there isn't someone queueing
            # Set the game ID for the player channel
            # Add a new game to the queue
            roomId = str(uuid.uuid4())
            player.setRoomId(roomId)
            self.room = Room(roomId)
            self.room.addPlayer(player)
            self.currentActiveRoomId = roomId
            roomMemberNumber = 1
            self.rooms[self.room.roomId] = self.room


        else:
            print("Room already created, connecting")

            # Set the game index for the currently connected channel
            player.setRoomId(self.currentActiveRoomId)

            # Set the second player channel
            self.room.addPlayer(player)
            # Send a message to the clients that the game is starting

            for i in range(0, self.room.numberOfMembers()):
                print("Sending start game event to players")
                self.room.getPlayer(i).getChannel().Send(
                        {"action": "startgame", "roomMember": i + 1, "playerId": self.room.getPlayer(i).getId(), "roomId": self.room.getRoomId()})

            # Add the game to the end of the game list

            # Empty the queue ready for the next connection
            self.room = None

            # Increment the game index for the next game
            # self.gameIndex += 1
        print("Number of rooms", len(self.rooms))
        print("Number of players in rooms" + str(self.rooms[self.currentActiveRoomId].numberOfMembers()))



    # Create a function to move the players of a game
    def movePlayer(self, x, y, moveAction, roomId, playerId, direction, time):

        # Get the game
        room = self.rooms[roomId]


        # For all the other players send a message to update their position
        for id in list(room.getPlayers().keys()):

            # If we aren't looking at the player that was updated
            if not id == playerId:
                # Send a message to update
                print("HERe" + str(time))
                room.getPlayerById(id).getChannel().Send(
                    {"action": moveAction, "playerId": id, "x": x, "y": y, "direction": direction, "time": time})



# Create the game class to hold information about any particular game
class Room(object):
    # Constructor
    def __init__(self, roomId):
        # Create a list of players
        self.players = {}

        self.channels = []
        # Store the network channel of the first client
        # Set the game id
        self.roomId = roomId

    def getRoomId(self):
        return self.roomId

    def addPlayer(self, player):
        self.players[player.getId()] = player
        self.channels = [player.getChannel()]

    def getPlayer(self, index):
        return list(self.players.values())[index]

    def getPlayerById(self, id):
        return self.players[id]

    def getPlayers(self):
        return self.players

    def getPlayersList(self):
        return list(self.players)

    def numberOfMembers(self):
        return len(self.players)


# Create a player class to hold all of our information about a single player
class Player(object):
    # Constructor
    def __init__(self, id, channel, x, y):
        # Set the x and y
        self.id = id
        self.channel = channel
        self.x = x
        self.y = y
        self.roomId = None

    def getId(self):
        return self.id

    def getChannel(self):
        return self.channel

    def setRoomId(self, roomId):
        self.roomId = roomId

    # Create a function to move this player
    def move(self, x, y):
        # Update the variables
        self.x += x
        self.y += y


# Start the server, but only if the file wasn't imported
if __name__ == "__main__":

    print("Server listening on " + str(SERVER_IP) + ":" + str(SERVER_PORT) + " ...\n")

    # Create a server
    s = GameServer()

    # Pump the server at regular intervals (check for new requests)
    while True:
        s.Pump()
        sleep(0.0001)