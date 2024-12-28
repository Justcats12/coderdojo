# Boardgame shop

### Professional: Easy

The goal of this lesson is to create an application for a board game store that lets us create and look up board games in different ways. The special feature of this application is to find a board game for a group of people according to the size of the group and how much time they have.

# Domain

The domain has two classes, `Boardgame` and `BoardgameShop`. The `Boardgame` class keeps track of the information about a boardgame and only has `__repr__` and `__str__` functions. The `BoardgameShop` class is a repository of boardgames that allows us so search and filter in different ways.

### repr and str?
Python classes have special functions that you can set to help with certain clauses. Two of these are `__repr__` (represent) and `__str__` (stringify). When defining both functions it is obligated to return a string item. The only difference between the 2 methods, is that `__repr__` is for robots and tech people (and all those in between). The `__str__` function is for normal people, e.g. someone's grandma.

tl,dr: `__str__` -> human readable output; `__repr__` -> computer readable output

Here's an example:
```python
class Ball:
    color = "red"
    radius = 10

    def __repr__(self):
        return f"Ball(color=\"{self.color}\",radius={self.radius})"
        # Ball(color="red",radius=10)

    def __str__(self):
        return f"{self.color.capitalize()} ball with radius {self.radius}cm"
        # Red ball with radius 10cm
```

## Step 1

Start with the `boardgame` class, it has 4 properties, name, maximum players, minimum players and time to play, which is 30 minutes by default. The `__init__` function includes all of the properties

```python
class Boardgame:
    def __init__(self, name : str, minPlayers : int, maxPlayers : int, time : int = 30):
        self.name = name
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.time = time
```

You can test if everything is working by making trying to make a Boardgame `b1` and testing if you can print all the properties

```python
# Testcode
b1 = Boardgame("abc", 1, 4, 15)
print(b1.name, b1.minPlayers) #...
```
## Step 2

Next we'll check if the properties are set correctly, any time or player amount of 0 or lower is invalid, and the maximum player amount has to be greater or equal to the minimum amount.

```python
class Boardgame:
    def __init__(self, name : str, minPlayers : int, maxPlayers : int, time : int = 30):
        assert minPlayers > 0, "Boardgame must need at least one player"
        assert minPlayers <= maxPlayers, "Max amount of players must be higher than min amount of players"
        assert time > 0, "Game cannot take 0 or less time to play"
        
        self.name = name
        self.minPlayers = minPlayers
        # ...
```

You can test this code by trying to make every type of incorrect Boardgame. Each one of the following should now cause an assertionerror.

```python
# testcode
b1 = Boardgame("A", -1, 2, 15)
b2 = Boardgame("B", 3, 2, 80)
b3 = Boardgame("C", 2, 4, 0)
```

## Step 3

Now make a `__repr__` function, this should return a string with every property as well as the class name. For example: 

`Boardgame(name="Uno",minPlayers=2,maxPlayers=4,time=15)`

You can check if it works with the following testcode:

```python
# testcode
b1 = Boardgame("Uno", 2, 4, 15)
print(repr(b1))
# Boardgame(name="Uno",minPlayers=2,maxPlayers=4,time=15)
```

Try to make this yourself before looking at the answer. You can find the answer below to check if you did it right.

```python
    def __repr__(self):
        return f"Boardgame(name=\"{self.name}\",minPlayers={self.minPlayers},maxPlayers={self.maxPlayers},time={self.time})"
```

## Step 4

Now try something similar with the `__str__` function. There only difference is that, if the time is over an hour the output is differnt, here are examples:

- Time under 1 hour: "Boardgame Uno, 2-4 players, 15 min playtime"
- Time over 1 hour: "Boardgame Monoploly, 2-6 players, 2:30 hrs playtime"

You can test it with the following testcode:

```python
# testcode
b1 = Boardgame("Uno", 2, 4, 15)
print(b1)
# BoardBoardgame Uno, 2-4 players, 15 min playtimegame 
b2 = Boardgame("Monoploly", 2, 6, 150)
print(b2)
# Boardgame Monoploly, 2-6 players, 2:30 hrs playtime
```

You can use either a normal if statement or a ternary if statement e.g.

```python
variable = value_when_true if condition else value_when_false
```

Try to write the code yourself, if you can fit it within 4-8 lines and it works that's good. If you need help here's the solution:

```python
    def __str__(self):
        hours = self.time // 60
        minutes =  self.time % 60
        time = f"{hours}:{minutes} hrs" if hours > 0 else f"{minutes} min"
        return f"Boardgame {self.name}, {self.minPlayers}-{self.maxPlayers} players, {time} playtime"
```

Now you're done with the `boardgame` class.

## Step 5

Now it's time for the `BoardgameShop` class, the only property it has is a list of strictly boardgames, as an extra you can make an assertion if the list given in the `__init__` is strictly boardgames. Go ahead and make the `__init__` 

```python
class BoardgameShop():
    def __init__(self, games : list[Boardgame]):
        self.games = games
```

## Step 6

Write a function that adds a boardgame to the list of boardgames. It first checks if the item being added is actually an instance of `Boardgame`, for this you can use the built-in `isinstance()` function.

```python
    def addBoardgame(self, game : Boardgame):
        assert isinstance(game, Boardgame), "New item must be a boardgame"
        self.games.append(game)
```

Test if everything is working by adding a Boardgame to the list and printing the list, then try to add something that isn't a board game, e.g. a string to the shop.

```python
# testcode
bgs = BoardgameShop([])
bgs.addBoardgame(Boardgame("A", 2, 4, 15))
print(bgs.games)
# prints list with the new board game in it
bgs.addBoardgame("hello")
# throws assertionerror
```

## Step 7

Now we'll add the first search function `findGameByName` which will find a boardgame by name. Use a for loop for this and return the first boardgame where the name is equal to the string (given as parameter). If it doesn't find anything it should return `None` instead.

Make a shop with 2-3 boardgames and see if it returns the correct one, you can use `print(bgs.findGameByName("name"))`. Since the `Boardgame` class has a `__str__` function it should print the human readable version of boardgame.

Try to make this yourself, the function should be 6-12 lines long. Don't forget to write a description fot this function.

```python
    def findGameByName(self, name : str):
        """Find a boardgame in this shop by name, returns the first boardgame it finds with the given name, returns None if nothing was found"""
        for g in self.games:
            if g.name == name:
                return g
        
        return None
```

## Step 8

The next search function `findGamesByPlayers` is a filter that looks for all the games that can be played by a given amount of players. The amount of players is given as a parameter. Then you check if it's not under the minimum player amount and over the maximum amount. Don't forget a description.

You can test this code by creating a `BoardgameShop` item and adding a few `Boardgame` items, then testing if a player count returns the correct items.

```python
# testcode
b1 = Boardgame("A", 2, 4, 10)
b2 = Boardgame("B", 1, 2)
b3 = Boardgame("C", 3, 4, 45)
bgs = BoardgameShop([b1, b2, b3])
print(bgs.findGamesByPlayers(3))
# A, C
print(bgs.findGamesByPlayers(2))
# A, B
```

Try to make the function yourself in 6-10 lines, start by making a new empty array, then append all boardgames where the player count fits. The return the new array.

If you can't figure it out you can use the example:

```python
    def findGamesByPlayers(self, players : int):
        """Returns a list of games that can be played by the given amount of players"""
        output = []

        for g in self.games:
            if g.minPlayers <= players <= g.maxPlayers:
                output.append(g)
        
        return output
```

## Step 9

We'll use this function in our next function `findPerfectGame` which finds a game returned by the previous function but closest to the given time. The player count and time are given by parameters. Start with making a new array that is equal to `self.findGamesByPlayers(players)`. Check if this array is empty first with an assertion. Don't forget a description.

Iterate over the new array and use the built in `abs()` function to check which game comes closest to the given time. The below function can be used to calculate how close two times are. The lower the number, the closer.

> |time1 - time2|

Try to do it yourself from here. If you need help here's some hints:

1) set the first best match to the first game in the list, then iterate over the rest
2) The condition `abs(time - g.time) < abs(time - bestGame.time)` must be true to set the next best match

If you can't figure it out with these hints, or want to check if your code is correct here's the example. Note that there were no instructions to return the first game if there's only one game, but this can make the code 

```python
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

```

The domain is now finished and we can start working on the cui.

# CUI

The cui or console user interface can be used to do 4 things.
1) Add a boardgame to the store
2) Search by name
3) Find games by amount of players
4) Find perfect game

## Step 1

The menu should look like this, and the user inputs the number of the option they want to do.

```
Type the number of the option you want to do
1) add a game
2) find game by name
3) find games by player amount
4) find perfect game
5) exit
```

This menu should be in a while loop with a match case, each option should be put in a separate function.

```python
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
```

## Step 2

When the user inputs 1 they should be asked for 4 things, the name (str), min player amount (int), max player amount (int), time (int). The experience should look something like this.

```
Name: Ludo
Minumum player amount: 2
Maxumum player amount: 4
Time to play (minutes): 20
```

As an extra you can make a helper function for inputting numbers, the function tries again after the user attempted an invalid input.

```python
def addGame():
    name = input("Name: ")
    minPlayers = inputNumber("Minumum player amount: ")
    maxPlayers = inputNumber("Maxumum player amount: ")
    time = inputNumber("Time to play (minutes): ")
    bgs.addBoardgame(Boardgame(name, minPlayers, maxPlayers, time))
```

## Step 3

Start by making a new `BoardgameShop` object and saving it to a variable `bgs`. All of the following should come ABOVE the while loop in the code

```python
bgs = BoardgameShop([])

# code comes here

# while...
```

Now implement all the other uptions into the cui in similar ways. Use inputs to ask for the different parameters and print the boardgames to the console. Since the `Boardgame` object has a `__str__` function this shouldn't be hard.

For the `findByName` function, check if `None` was returned, if so this means that there was no board game with that name found. Print a fitting message.

For the `findByPlayers` function, multiple answers are possible, so you have to iterate over every answer and print it in a numbered way.

```
1) Boardgame Uno, 2-6 players, 15 min playtime
2) Boardgame Scyte, 2-6 players, 1:0 hrs playtime
3) Boardgame Wingspan, 2-4 players, 30 min playtime
```
Try to make these functions yourself, if you want to check if you did it correctly or if you need help here's the example.

```python
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

# while...
```

# Extra

The instructions included some extras:

1) Assert if all objects entered into a new `BoardgameShop` are of the instance `Boardgame` (in one line).
2) Make a helper function for inputting numbers using a try-except block.

Extras not mentioned in instructions

3) Make the cui completely robust, with try-execpt blocks anywhere where an exception can take place.
4) Add a function to the `BoardgameShop` class `findByTimeLimit`, that is similar to `findPerfectGame`, except it excludes all games that are above the given time. Implement it into the cui as well.

# Entire code

If your code should be working properly, but it isn't you can check the full code here to see if you misplaced/forgot something

```python
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
```