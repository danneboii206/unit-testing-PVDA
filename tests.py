import pytest
import interactWithObj as interact

def test_SelectObj():
    '''test event 1 and 2 in Assignment Input: Detailed Use Case (Interact with Object) + System Sequence Diagram'''
    game = interact.Game()

    assert game.selectObject("apple") == "PickUp\nDrop\nTaste\nMove\nLook\n"
    assert game.selectObject("chest") == "Open\nLook\nMove\nPickUp\nDrop\n"

    

def test_SelectInteraction():
    '''test event 3 & 4'''
    apple = interact.Game()
    apple.selectObject("apple")

    chest = interact.Game()
    chest.selectObject("chest")

    dropOptions = ["carefully", "nonchalantly"]
    pickupOptions = ["carefully", "normally"]
    lookOptions = ["inspect", "vaguely"]
    openOptions = ["carefully", "quickly"]
    moveOptions = ["carefully", "aggressively"]
    turnOptions = [""]
    tasteOptions = ["little", "alot"]

    assert apple.currentGameObj.selectCurrentInteraction("PickUp") == pickupOptions
    assert apple.currentGameObj.selectCurrentInteraction("Drop") == dropOptions
    assert apple.currentGameObj.selectCurrentInteraction("Taste") == tasteOptions
    assert apple.currentGameObj.selectCurrentInteraction("Move") == moveOptions
    assert apple.currentGameObj.selectCurrentInteraction("Look") == lookOptions

    assert chest.currentGameObj.selectCurrentInteraction("Open") == openOptions
    assert chest.currentGameObj.selectCurrentInteraction("Look") == lookOptions
    assert chest.currentGameObj.selectCurrentInteraction("Move") == moveOptions
    assert chest.currentGameObj.selectCurrentInteraction("PickUp") == pickupOptions
    assert chest.currentGameObj.selectCurrentInteraction("Drop") == dropOptions

def test_hello():
    '''
    event 3 & 4 failure test
    '''
    apple = interact.Game()
    apple.selectObject("apple")

    chest = interact.Game()
    chest.selectObject("chest")

    assert apple.currentGameObj.selectCurrentInteraction("Monkey") == "Not an option!"
    assert chest.currentGameObj.selectCurrentInteraction("Monkey") == "Not an option!"
    assert apple.currentGameObj.selectCurrentInteraction("jfiqor") == "Not an option!"
    assert chest.currentGameObj.selectCurrentInteraction("qokjropqkr") == "Not an option!"

def test_setOptionsStartInteraction():
    apple = interact.Game()
    apple.selectObject("apple")

    chest = interact.Game()
    chest.selectObject("chest")
    '''
    self._apple = GameObject("apple", ["PickUp", "Drop", "Taste", "Move", "Look"])
    self._chest = GameObject("chest", ["Open", "Look", "Move", "PickUp", "Drop"])

    pickupOptions = ["carefully", "normally"]
    dropOptions = ["carefully", "nonchalantly"]
    lookOptions = ["inspect", "vaguely"]
    openOptions = ["carefully", "quickly"]
    moveOptions = ["carefully", "aggressively"]
    turnOptions = [""]
    tasteOptions = ["little", "alot"]

    RES=     interaction pickup started with options['carefully']...
    '''

    apple.currentGameObj.selectInteraction("PickUp")
    apple.currentGameObj.setInteractionOptions("carefully")
    assert apple.currentGameObj.startInteraction() == "interaction pickup started with options['carefully']..."

    apple.currentGameObj.selectInteraction("PickUp")
    apple.currentGameObj.setInteractionOptions("normally")
    assert apple.currentGameObj.startInteraction() == "interaction pickup started with options['normally']..."

    apple.currentGameObj.selectInteraction("Drop")
    apple.currentGameObj.setInteractionOptions("carefully")
    assert apple.currentGameObj.startInteraction() == "interaction drop started with options['carefully']..."

    apple.currentGameObj.selectInteraction("Drop")
    apple.currentGameObj.setInteractionOptions("nonchalantly")
    assert apple.currentGameObj.startInteraction() == "interaction drop started with options['nonchalantly']..."

    apple.currentGameObj.selectInteraction("Look")
    apple.currentGameObj.setInteractionOptions("vaguely")
    assert apple.currentGameObj.startInteraction() == "interaction look started with options['inspect']..."

    apple.currentGameObj.selectInteraction("Look")
    apple.currentGameObj.setInteractionOptions("vaguely")
    assert apple.currentGameObj.startInteraction() == "interaction look started with options['inspect']..."
