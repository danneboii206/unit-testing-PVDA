import interactWithObj as interact

def main():
    stop = False

    while not stop:
        print("\nAvailable objects:\n")
        game = interact.Game()

        usrInput = input("Select game object OR q to quit: ")
        if usrInput == "q":
            break
        res = game.selectObject(usrInput)
        while res == None and res != "q":
            usrInput = input("Select game object OR q to quit: ")
            res = game.selectObject(usrInput)

        print(f"\nAvailable interactions:\n{res}")
        usrInput = input("Select interaction: ")
        res = game.currentGameObj.selectInteraction(usrInput)
        while res == "Not an option!":
            print(res)
            usrInput2 = input("Select interaction: ")
            res =  game.currentGameObj.selectInteraction(usrInput2)
        print(f"\nSelect interaction options:\n{res}")
        usrInput = input("Enter Options split with (,): ")
        game.currentGameObj.setInteractionOptions(usrInput)
        print(game.currentGameObj.startInteraction())

if __name__ == "__main__":
    main()
