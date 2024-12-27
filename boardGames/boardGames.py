#
# Domain
#
class Boardgame:
    def __init__(self, name : str, minPlayers : int, maxPlayers : int, time : int = 30):
        assert minPlayers > 0, "Boardgame must need at least one player"
        assert minPlayers <= maxPlayers, "Max amount of players must be higher than min amount of players"
        assert time > 0, "Game cannot take 0 or less time to play"
        
        self.name = name
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.time = time
    def __repr__(self):
        return f"Boardgame(name=\"{self.name}\",minPlayers={self.minPlayers},maxPlayers={self.maxPlayers},time={self.time})"
    def __str__(self):
        hours = self.time // 60
        minutes =  self.time % 60
        time = f"{hours}:{minutes} hrs" if hours > 0 else f"{minutes} min"
        return f"Boardgame {self.name}, {self.minPlayers}-{self.maxPlayers} players, {time} playtime"

class BoardgameShop():
    def __init__(self, games : list[Boardgame]):
        assert all([isinstance(i, Boardgame) for i in games]), "All objects must be boardgame" # extra
        self.games = games
    
    def addBoardgame(self, game : Boardgame):
        assert isinstance(game, Boardgame), "New item must be a boardgame"
        self.games.append(game)
    
    def findGameByName(self, name : str):
        """Find a boardgame in this shop by name, returns the first boardgame it finds with the given name, returns None if nothing was found"""
        for g in self.games:
            if g.name == name:
                return g
        
        return None
    
    def findGamesByPlayers(self, players : int):
        """Returns a list of games that can be played by the given amount of players"""
        output = []

        for g in self.games:
            if g.minPlayers <= players <= g.maxPlayers:
                output.append(g)
        
        return output
    
    def findPerfectGame(self, players : int, time : int):
        """Returns a game that can be played by the amount of players and is closest to the given time
        
        Throws exception if no games were found
        """

        games = self.findGamesByPlayers(players)

        assert len(games) > 0, "No games found for the amount of players"
        if len(games) == 1:
            return games[0]
        
        bestGame = games[0]

        for g in games[1:]:
            if abs(time - g.time) < abs(time - bestGame.time):
                bestGame = g
        
        return bestGame

#
# Cui
#

bgs = BoardgameShop([]) 

def inputNumber(prompt : str): # extra
    num = input(prompt)
    try:
        return int(num)
    except:
        print(f"{num} is not a valid input, please enter a number.")
        inputNumber(prompt)

def addGame():
    name = input("Name: ")
    minPlayers = inputNumber("Minumum player amount: ")
    maxPlayers = inputNumber("Maxumum player amount: ")
    time = inputNumber("Time to play (minutes): ")
    bgs.addBoardgame(Boardgame(name, minPlayers, maxPlayers, time))


def findGameByName():
    name = input("Enter name: ")
    game = bgs.findGameByName(name)

    if game is None:
        print("404 game not found")
    else:
        print(game)
    

def findGamesByPlayerAmount():
    players = inputNumber("Player amount: ")
    games = bgs.findGamesByPlayers(players)

    for i,g in enumerate(games):
        print(f"{i+1}) {g}")

def findPerfectGame():
    players = inputNumber("Player amount: ")
    time = inputNumber("Time available: ")

    game = bgs.findPerfectGame(players, time)

    print(game)

keepGoing = True
while keepGoing:
    print("""
Type the number of the option you want to do
1) add a game
2) find game by name
3) find games by player amount
4) find perfect game
5) exit
    """)
    option = input("Option: ")
    match option:
        case "1":
            addGame()
        case "2":
            findGameByName()
        case "3":
            findGamesByPlayerAmount()
        case "4":
            findPerfectGame()
        case "5":
            keepGoing = False
        case _:
            print("Invalid option, please enter the number corresponding to an option.")