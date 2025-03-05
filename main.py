import pytest
import interactWithObj as interact

def main():
    game1 = interact.game()
    usrInput = input("Select game object: ")
    game1.selectObject(usrInput)

if __name__ == "__main__":
    main()