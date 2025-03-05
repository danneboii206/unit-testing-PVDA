from abc import ABC, abstractmethod 

class game:
    def __init__(self):
        self._scene1 = scene()
        self._scene1.listAvailableElements()

    def selectObject(self, theGameObject): #why is it string??
        self._curretGameObj = self._scene1.isAvailable(theGameObject)
        if self._curretGameObj != None: #check if object exist
            return self._curretGameObj.listInteractionTypes() #if exist return interactions
        return ""

    def selectInteraction(self, theInteraction):
        if theInteraction in self._curretGameObj.listInteractionTypes():
            print(theInteraction)
            print("true")
        else:
            print("false")
        
class scene:
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
        for element in self._gameObjList:
            if gameElement == element.name:
                return element
        return None

class GameObject:
    def __init__(self, name, interactions):
        self.name = name
        self._interactionTypes = []
        self._AcceptedInteractions = ["PickUp", "Drop", "Taste", "Move", "Look", "Open", "TurnOn", "TurnOff"]
        for interaction in interactions:
            self.identifyInteractionType(interaction)
        pass

    def identifyInteractionType(self, theInteraction): #gameobject has to create its own interactions
        if theInteraction in self._AcceptedInteractions:
            match theInteraction:
                case "Drop":
                    newInteraction = (Drop(), theInteraction)
                case "PickUp":
                    newInteraction = (PickUp(), theInteraction)
                case "Taste": 
                    newInteraction = (Taste(), theInteraction)
                case "Move":
                    newInteraction = (Move(), theInteraction)
                case "Look":
                    newInteraction = (Look(), theInteraction)
                case "Open":
                    newInteraction = (Open(), theInteraction)
                case "TurnOn": 
                    newInteraction = (TurnOn(), theInteraction)
                case "TurnOff":
                    newInteraction = (TurnOff(), theInteraction)
                case _:
                    raise ValueError(f"Unknown interaction: {theInteraction}")  # Handle unexpected input

            self._interactionTypes.append(newInteraction)

    def listInteractionTypes(self):
        interactionStr = ""
        for interaction in self._interactionTypes:
            interactionStr += f"{interaction[1]}\n"            
        return interactionStr
#     def startInteraction(theInteractionType):
    
#     def listcurrentInteractionOptions():

#     def setCurrentInteractionOptions():

class InteractionType(ABC):
    def __init__(self):
        self._interactionOptions = ["now", "later", "aggressively", "gently"]
        super().__init__()
    @abstractmethod
    def startInteraction(self):
        pass
    @abstractmethod
    def getAvailableOptions(self):
        pass

class Drop(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction drop started...")
        return super().startInteraction()
        
class PickUp(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction pickup started...")
        return super().startInteraction()
class Look(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction look started...")
        return super().startInteraction()
class Open(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction open started...")
        return super().startInteraction()
class Move(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction move started...")
        return super().startInteraction()
class TurnOn(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction turnon started...")
        return super().startInteraction()
class TurnOff(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction turnoff started...")
        return super().startInteraction()
class Taste(InteractionType):
    def __init__(self):
        super().__init__()
    def getAvailableOptions(self):
        for option in self._interactionOptions:
            print(option)
        return super().getAvailableOptions()
    def startInteraction(self):
        print("interaction taste started...")
        return super().startInteraction()