import pytest
import interactWithObj

def test_SelectObj(): #test event 1 and 2 in Assignment Input: Detailed Use Case (Interact with Object) + System Sequence Diagram
    game1 = interactWithObj.Game()
    assert game1.selectObject("apple") == "PickUp\nDrop\nTaste\nMove\nLook\n"
    assert game1.selectObject("doesnt exist") == ""

def test_SelectOption():
    allInteractions = ["PickUp", "Drop", "Taste", "Move", "Look", "Open", "TurnOn", "TurnOff"]
    game2 = interactWithObj.Game()
    game2.selectObject("apple")

    #check if valid interactions return right interaction options
    assert game2.selectInteraction("PickUp") == "['now', 'later', 'aggressively', 'gently']"
    assert game2.selectInteraction("Drop") == "['now', 'later', 'aggressively', 'gently']"
    assert game2.selectInteraction("Taste") == "['now', 'later', 'aggressively', 'gently']"
    assert game2.selectInteraction("Move") == "['now', 'later', 'aggressively', 'gently']"
    assert game2.selectInteraction("Look") == "['now', 'later', 'aggressively', 'gently']"

    #check if invalid interactions return correct response
    assert game2.selectInteraction("TurnOn") == "Not A Option!"
    assert game2.selectInteraction("TurnOff") == "Not A Option!"
    assert game2.selectInteraction("Open") == "Not A Option!"

    #check random value
    assert game2.selectInteraction("monkey") == "Not A Option!"
    assert game2.selectInteraction(23) == "Not A Option!"

    