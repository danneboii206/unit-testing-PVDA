import pytest
import interactWithObj as interact

def main():
    game1 = interact.Game()
    usrInput = input("Select game object: ")
    print(game1.selectObject(usrInput))
    usrInput = input ("Select interaction: ")
    print(game1.selectInteraction(usrInput))

if __name__ == "__main__":
    main()