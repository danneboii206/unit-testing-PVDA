import pytest
import interactWithObj as interact

def test_SelectObj():
    '''test event 1 and 2 in Assignment Input: Detailed Use Case (Interact with Object) + System Sequence Diagram'''
    game = interact.Game()

    assert game.selectObject("apple") == "PickUp\nDrop\nTaste\nMove\nLook\n"
    assert game.selectObject("chest") == "Open\nLook\nMove\nPickUp\nDrop\n"
        
    with pytest.raises(NameError) as err:
        game.selectObject("iaoghfioaj")
    assert err.type is NameError
    
def test_SelectInteraction(): 
    '''test event 3 and 4'''
    apple = interact.Game()
    apple.selectObject("apple")

    chest = interact.Game()
    chest.selectObject("chest")

    applePossibleInteractions = ["PickUp", "Drop", "Taste", "Move", "Look"]
    chestPossibleInteractions = ["Open", "Look", "Move", "PickUp", "Drop"]

    appleWrongInteractions = ["TurnOn", "TurnOff", "Open"]
    chestWrongInteractions = ["TurnOn", "TurnOff", "Taste"]

    randomVals = {"Monkey", 23}

    resStrAccepted = "['now', 'later', 'aggressively', 'gently']"
    resStrDenied = "Not an option!"

    #check if valid interactions return right interaction options
    for element in applePossibleInteractions:
        assert apple.selectInteraction(f"{element}") == resStrAccepted
    for element in appleWrongInteractions:
        assert apple.selectInteraction(f"{element}") == resStrDenied

    for element in chestPossibleInteractions:
        assert chest.selectInteraction(f"{element}") == resStrAccepted
    for element in chestWrongInteractions:
        assert chest.selectInteraction(f"{element}") == resStrDenied

    #check random value
    for element in randomVals:
        assert apple.selectInteraction(f"{element}" == resStrDenied)
    for element in randomVals:
        assert chest.selectInteraction(f"{element}" == resStrDenied)
