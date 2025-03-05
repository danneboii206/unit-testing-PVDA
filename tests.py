import pytest
import interactWithObj

def test_SelectObj(): #test event 1 and 2 in Assignment Input: Detailed Use Case (Interact with Object) + System Sequence Diagram
    game1 = interactWithObj.Game()
    assert game1.selectObject("apple") == "PickUp\nDrop\nTaste\nMove\nLook\n"
    assert game1.selectObject("doesnt exist") == ""

    #SKRIV TESTER FÖR CHEST
    
def test_SelectInteraction(): #test event 3 and 4
    game2 = interactWithObj.Game()
    game2.selectObject("apple")
    applePossibleInteractions = ["PickUp", "Drop", "Taste", "Move", "Look"]
    appleWrongInteractions = ["TurnOn", "TurnOff", "Open"]
    resStr = "['now', 'later', 'aggressively', 'gently']"

    #check if valid interactions return right interaction options
    for element in applePossibleInteractions:
        assert game2.selectInteraction(f"{element}") == resStr

    for element in appleWrongInteractions:
        assert game2.selectInteraction(f"{element}") == "Not A Option!"

    #check random value
    assert game2.selectInteraction("monkey") == "Not A Option!"
    assert game2.selectInteraction(23) == "Not A Option!"

    #SKRIV TESTER FÖR CHEST