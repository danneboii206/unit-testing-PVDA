import pytest
import interactWithObj as interact

def main():
    stop = False
    while not stop:
        print("\nAvailable objects:\n")
        game = interact.Game()
        usrInput = input("Select game object OR q to quit: ")
        if usrInput == "q":
            break
        print("\nAvailable interactions:\n")
<<<<<<< Updated upstream
        print(game1.selectObject(usrInput))
        usrInput = input ("Select interaction: ")
        print(f"\nSelect interaction options:\n{game1.selectInteraction(usrInput)}")

=======
        print(game.selectObject(usrInput))
        usrInput2 = input("Select interaction: ")
        res =  game.currentGameObj.selectInteraction(usrInput2)
        while res == "Not an option!":
            print(res)
            print(game.selectObject(usrInput))
            usrInput2 = input("Select interaction: ")
            res =  game.currentGameObj.selectInteraction(usrInput2)
        print(f"\nSelect interaction options:\n{res}")
        usrInput = input("Enter Options split with (,): ")
        game.currentGameObj.setInteractionOptions(usrInput)
        print(game.currentGameObj.startInteraction())
>>>>>>> Stashed changes
if __name__ == "__main__":
    main()
