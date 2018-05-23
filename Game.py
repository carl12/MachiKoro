
import random
import Cards
import Player


def roll1():
    return random.randrange(5) + 1


def roll2():
    a = roll1()
    b = roll1()
    return [a + b, a == b]


class Game():
    def __init__(self, players=None):
        self.buildList = [Cards.Farm(), Cards.Ranch(), Cards.Bakery(), Cards.Cafe(), Cards.ConvenienceStore()]
        self.buildDict = {b.name:b for b in self.buildList}
        if players:
            self.players = players
        else:
            self.players = [Player.Player(self, 0), Player.Player(self, 1), Player.Player(self, 2)]


    def play_game(self):
        game_over = False
        for i in range(100):
            for p in self.players:
                self.take_turn(p)
                if p.has_won():
                    print(p ,"won!")
                    game_over = True
            if game_over:
                print("Game Over!")
                break
        else:
            print("Game ended after 100 rounds")

    def take_turn(self, p):
        extra_turn = self.roll(p)
        p.choose_buy()
        if extra_turn:
            self.take_turn(p)

    def roll(self, p, used_radio = False):
        extra_turn = False
        doubles = False
        if not p.landmarks[0].owned:
            if p.roll2():
                rolls = roll2()
                roll = rolls[0]
                doubles = rolls[1]
            else:
                roll = roll1()
        else:
            roll = roll1()
        if not used_radio and p.landmarks[3].owned and p.reroll(roll,doubles):
            return self.roll(p,True)
        else:
            self.give_rewards(roll, p)
            return doubles

    def take(self, loc):
        return self.buildList[loc].buy()



    def give_rewards(self, roll, player):
        print(roll, "was rolled")
        for p in self.players:
            p.get_reward(roll, p == player)

    def get_remain(self):
        return [b.remain for b in self.buildList]

    def get_name_remain(self):
        return [b.name+" "+str(b.remain) for b in self.buildList]