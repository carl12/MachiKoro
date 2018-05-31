
import random
import itertools

import Cards
import Player
import GameState

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
        self.turn_state = GameState.TurnState(0,0,0,0)
        if players:
            self.players = players
        else:
            self.players = [Player.Player(self, 0), Player.Player(self, 1), Player.Player(self, 2)]


    def play_game(self):
        game_over = False
        for i in range(100):
            self.turn_state.player_turn = 0
            for p in self.players:
                self.take_turn(p)
                if p.has_won():
                    print(p ,"won!")
                    game_over = True
            if game_over:
                #set turn state to after last player if game over
                self.turn_state.player_turn = len(self.players)
                print("Game Over!")
                break
            self.turn_state.player_turn += 1
        else:
            print("Game ended after 100 rounds")

    def take_turn(self, p, first_turn = True):

        self.turn_state.set_pre_roll(first_turn)
        roll,extra_turn = self.roll(p)

        print('roll is ',roll)
        self.turn_state.set_resolving_roll(first_turn)
        self.give_rewards(roll, p)

        self.turn_state.set_buying(first_turn)
        p.choose_buy()

        if extra_turn:
            self.take_turn(p,False)

    def roll(self, p, used_radio = False):
        extra_turn = False
        doubles = False
        if p.landmarks[0].owned:
            if p.roll2():
                roll,doubles = roll2()
            else:
                roll = roll1()
        else:
            roll = roll1()
        if  p.landmarks[3].owned and not used_radio and p.reroll(roll,doubles):
            return self.roll(p,True)
        else:
            return roll,doubles

    def take(self, loc):
        return self.buildList[loc].buy()



    def give_rewards(self, roll, player):
        # note this sequencing is incorrect
        # Order should be red for each, then blue/(other), then purple for all

        loc = self.players.index(player)
        last = len(self.players)
        list =  itertools.chain(reversed(range(0,loc)),reversed(range(loc,last)))
        for i in list:
            p = self.players[i]
            self.turn_state.pending_player = i
            p.get_reward(roll, p == player, self.turn_state)


    def get_remain(self):
        return [b.remain for b in self.buildList]

    def get_name_remain(self):
        return [b.name+" "+str(b.remain) for b in self.buildList]

    def get_state(self):
        remain = [x.remain for x in self.buildList]
        turn_state = self.turn_state
        roll=0
        players = [p.state() for p in self.players]
        return  GameState.GameState(remain,turn_state,roll,players)