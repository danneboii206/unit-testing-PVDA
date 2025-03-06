import pytest
import interactWithObj as interact

def main():
    stop = False
    while not stop:
        print("\nAvailable objects:\n")
        game1 = interact.Game()
        usrInput = input("Select game object OR q to quit: ")
        if usrInput == "q":
            break
        print("\nAvailable interactions:\n")
        print(game1.selectObject(usrInput))
        usrInput = input("Select interaction: ")
        print(f"\nSelect interaction options:\n{game1.currentGameObj.selectInteraction(usrInput)}")
        usrInput = input("Enter Options split with (,): ")
        game1.currentGameObj.setInteractionOptions(usrInput)
        print(game1.currentGameObj.startInteraction())
if __name__ == "__main__":
    main()
