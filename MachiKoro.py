import Game
import GameState

game = Game.Game()
print(game.get_state().get_json())
game.play_game()
print("Done")

