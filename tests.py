import pytest
import interactWithObj

def testSelect():
    game1 = interactWithObj.game()
    assert game1.selectObject("apple") == True
    assert game1.selectObject("elevator") == False