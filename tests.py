import pytest
import interactWithObj

def testSelect(): #test event 1 and 2 in Assignment Input: Detailed Use Case (Interact with Object) + System Sequence Diagram
    game1 = interactWithObj.game()
    assert game1.selectObject("apple") == "PickUp\nDrop\nTaste\nMove\nLook\n"
    assert game1.selectObject("doesnt exist") == ""
