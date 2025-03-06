from abc import ABC, abstractmethod

class Game:
    def __init__(self):
        self._scene1 = Scene()
        self._scene1.listAvailableElements()
       
    def selectObject(self, theGameObject):
        GameObj = self._scene1.isAvailable(theGameObject)
        if GameObj != None:
            self.currentGameObj = GameObjInterface(GameObj)
            return GameObj.listInteractionTypes() #if exist return interactions
        else:
            return None

class GameObjInterface:
    def __init__(self, GameObj):
        self._currentGameObj = GameObj

    def selectInteraction(self, theInteraction):
        try:
            if theInteraction in self._currentGameObj.listInteractionTypes():
                self._currentGameObj.setCurrentInteraction(theInteraction)
        except TypeError: #Fixes when someone uses integers instead of strings (shouldn't be possible anyways as input returns string)
            return "Not an option!"
        else:
            try:
                return self._currentGameObj.listCurrentInteractionOptions()
            except AttributeError:
                return "Not an option!"
    def setInteractionOptions(self, theOptions):
        options = theOptions.split(",")
        return self._currentGameObj.setCurrentInteractionOptions(options)
    
    def startInteraction(self):
        return self._currentGameObj.startInteraction()
<<<<<<< Updated upstream

=======
        
>>>>>>> Stashed changes
class Scene:
    def __init__(self):
        self._gameObjList = []
        self._apple = GameObject("apple", ["PickUp", "Drop", "Taste", "Move", "Look"])
        self._chest = GameObject("chest", ["Open", "Look", "Move", "PickUp", "Drop"])
        self._gameObjList.append(self._apple)
        self._gameObjList.append(self._chest)

    def listAvailableElements(self):
        for gameObj in self._gameObjList:
            print(gameObj.name)

    def isAvailable(self, gameElement):
        for element in self._gameObjList: #check if object exists
            if gameElement == element.name:
                return element
        return None

class GameObject:
    def __init__(self, name, interactions):
        self.name = name
        self._interactionTypes = []
        self._AcceptedInteractions = ["PickUp", "Drop", "Taste", "Move", "Look", "Open", "TurnOn", "TurnOff"] 
        self._currentInteraction = ""

        for interaction in interactions:
            self.identifyInteractionType(interaction)

    def identifyInteractionType(self, theInteraction): #gameobject has to create its own interactions
        if theInteraction in self._AcceptedInteractions:
            self._interactionTypes.append(theInteraction)

    def listInteractionTypes(self):
        interactionStr = ""
        for interaction in self._interactionTypes:
            interactionStr += f"{interaction}\n"          
        return interactionStr

    def setCurrentInteraction(self, theInteraction): #pure fabrication
        match theInteraction:
            case "Drop":
                self._currentInteraction = Drop()
            case "PickUp":
                self._currentInteraction = PickUp()
            case "Taste":
                self._currentInteraction = Taste()
            case "Move":
                self._currentInteraction = Move()
            case "Look":
                self._currentInteraction = Look()
            case "Open":
                self._currentInteraction = Open()
            case "TurnOn":
                self._currentInteraction = TurnOn()
            case "TurnOff":
                self._currentInteraction = TurnOff()
            case _:
                raise ValueError(f"Unknown interaction: {theInteraction}")  # Handle unexpected input, should not be possible at this point

    def listCurrentInteractionOptions(self):
        return f"{self._currentInteraction.availableInteractionOptions}"

    def setCurrentInteractionOptions(self, options):
        return self._currentInteraction.setInteractionOptions(options)

    def startInteraction(self):
        return self._currentInteraction.startInteraction()


class InteractionType(ABC):
    def __init__(self):
        self._interactionOptions = []
        super().__init__()

    @property
    @abstractmethod
    def availableInteractionOptions(self): 
        pass

    def setInteractionOptions(self, options):
        for option in options:
            if option not in self.availableInteractionOptions:
                options.remove(option)

        for option in options:
            self._interactionOptions.append(option)

    @abstractmethod
    def startInteraction(self):
        pass

class Drop(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "nonchalantly"] 

    def startInteraction(self):
        return f"interaction drop started with options{self._interactionOptions}..."

class PickUp(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "normaly"] 

    def startInteraction(self):
        return f"interaction pickup started with options{self._interactionOptions}..."

class Look(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully",] 

    def startInteraction(self):
        return f"interaction look started with options{self._interactionOptions}..."

class Open(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully",]
    
    def startInteraction(self):
        return f"interaction open started with options{self._interactionOptions}..."

class Move(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "aggressively",] 

    def startInteraction(self):
        return f"interaction move started with options{self._interactionOptions}..."

class TurnOn(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["",] 

    def startInteraction(self):
        return f"interaction turnon started with options{self._interactionOptions}..."

class TurnOff(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["",] 

    def startInteraction(self):
        return f"interaction turnoff started with options{self._interactionOptions}..."

class Taste(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["little", "alot"] 
    
    def startInteraction(self):
        return f"interaction taste started with options{self._interactionOptions}..."