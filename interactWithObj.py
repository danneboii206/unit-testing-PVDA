from abc import ABC, abstractmethod 

class game:
    def __init__(self):
        self._scene1 = scene()
        self._scene1.listAvailableElements()

    def selectObject(self, theGameObject):
        return self._scene1.isAvailable(theGameObject)

class scene:
    def __init__(self):
        self._gameObjList = []
        self._apple = GameObject("apple", ["PickUp", "drop", "Taste", "Move", "Look"])
        self._chest = GameObject("chest", ["Open", "look"])
        self._gameObjList.append(self._apple)
        self._gameObjList.append(self._chest)

    def listAvailableElements(self):
        for gameObj in self._gameObjList:
            print(gameObj)

    def isAvailable(self, gameElement):
        for element in self._gameObjList:
            return gameElement == element.name


class GameObject:
    def __init__(self, name, interactions):
        self.name = name
        # for interaction in interactions:
        #     objInteraction = InteractionType()
        pass
    # def listInteractionTypes():

#     def startInteraction(theInteractionType):
    
#     def listcurrentInteractionOptions():

#     def setCurrentInteractionOptions():

# class GameObjectRepository:
#     def __init__(self):
#         pass

# class InteractionType:
#     @abstractmethod
#     def identifyInteraction(self, theInteractionType):
#         pass
#     @abstractmethod
#     def setInteractionOptions(self):
#         pass
#     @abstractmethod
#     def startInteraction(self):
#         pass
#     @abstractmethod
#     def getAvvilableOptions(self):
#         pass