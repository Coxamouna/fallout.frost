import game

def main():
    gamerun = game.Game(game.WIDTH, game.HEIGHT, game.NAME, game.FPS)
    gamerun.run()

if __name__ == "__main__":
    main()