from abc import ABC, abstractmethod

class Game:
    def __init__(self):
        self.currentGameObj = ""
        self._scene1 = Scene()
        self._scene1.listAvailableElements()
        self._curretGameObj = ""
    def selectObject(self, theGameObject):
        self._curretGameObj = self._scene1.isAvailable(theGameObject)
        if self._curretGameObj != None:
            return self._curretGameObj.listInteractionTypes() #if exist return interactions
        raise NameError("No such object")

    def selectInteraction(self, theInteraction):
        try:
            if theInteraction in self._curretGameObj.listInteractionTypes():
                self._curretGameObj.setCurrentInteraction(theInteraction)
        except TypeError: #Fixes when someone uses integers instead of strings (shouldn't be possible anyways as input returns string)
            return "Not an option!"
        else:
            try:
                return self._currentGameObj.listCurrentInteractionOptions()
            except AttributeError:
                return "Not an option!" #inputting wrong option ends in exception
    def setInteractionOptions(self, theOptions):
        options = theOptions.split(",")
        return self._currentGameObj.setCurrentInteractionOptions(options)
    
    def startInteraction(self):
        return self._currentGameObj.startInteraction()

class Scene:
    def __init__(self):
        self._gameObjList = []
        self._apple = GameObject("apple", ["PickUp", "Drop", "Taste", "Move", "Look"])
        self._chest = GameObject("chest", ["Open", "Look", "Move", "PickUp", "Drop"])
        self._light = GameObject("light", ["TurnOn", "TurnOff"])
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
#     def startInteraction(theInteractionType):

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
        return self._currentInteraction.availableInteractionOptions

#     def setCurrentInteractionOptions():

class InteractionType(ABC):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def availableInteractionOptions(self):
        pass

    @abstractmethod
    def startInteraction(self):
        pass

    @abstractmethod
    def getAvailableOptions(self):
        pass

class Drop(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "nonchalantly"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        if self._interactionOptions in ["carefully", "nonchalantly"]:
            return f"interaction drop started with options{self._interactionOptions}..."
        else:
            return "Not an option!"

class PickUp(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "normally"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction pickup started...")
        return super().startInteraction()

class Look(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["inspect", "vaguely"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction look started...")
        return super().startInteraction()

class Open(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "quickly"]
    
    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction open started...")
        return super().startInteraction()

class Move(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["carefully", "aggressively"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction move started...")
        return super().startInteraction()

class TurnOn(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["fast", "slowly"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction turnon started...")
        return super().startInteraction()

class TurnOff(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["fast", "slowly"]

    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction turnoff started...")
        return super().startInteraction()

class Taste(InteractionType):
    @property
    def availableInteractionOptions(self):
        return ["little", "alot"] 
    
    def getAvailableOptions(self):
        for option in self._availableInteractionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction taste started...")
        return super().startInteraction()
