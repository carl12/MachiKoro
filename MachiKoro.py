# 1 - farm 
# 2 - ranch
# 2/3 - Bakery
# 3 - cafe
# 4 - convenience store
# 5 - forest
# 6 - stadium/tv station/business center
# 7 - cheese factory
# 8 - furniture factory
# 9 - mine 
# 9/10 - Family restaurant
# 10 - apple orchard
# 11-12 fruit/vegetable stand

import random


class Card:
    trigger = [0]
    on_turn = False
    off_turn = False
    reward = 0
    cost = 0
    quantity = 10
    public_card = True

    def buy(self):
        if self.quantity > 0:
            self.quantity = self.quantity - 1
            return self

    def check(self, roll, is_turn):
        if (is_turn and self.on_turn) or (not is_turn and self.off_turn):
            if roll in self.trigger:
                return self.get_reward()

    def get_reward(self):
        return self.reward


class Farm(Card):
    name = "Farm"
    trigger = [1]
    on_turn = True
    off_turn = True
    reward = 1
    cost = 1
    quantity = 6


class Ranch(Card):
    name = "Ranch"
    trigger = [2]
    on_turn = True
    off_turn = True
    reward = 1
    cost = 1
    quantity = 6


class Bakery(Card):
    name = "Bakery"
    trigger = [2, 3]
    on_turn = True
    off_turn = False
    reward = 1
    cost = 1
    quantity = 6


class Cafe(Card):
    name = "Cafe"
    trigger = [3]
    on_turn = False
    off_turn = True
    reward = 1
    cost = 2
    quantity = 6

    def get_reward(self):
        return self.reward


class ConvenienceStore(Card):
    name = "Convenience Store"
    trigger = [4]
    on_turn = True
    off_turn = True
    reward = 3
    cost = 2
    quantity = 6


class Station(Card):
    name = "Station"
    cost = 4
    quantity = 1
    public_card = False


class ShoppingMall(Card):
    name = "Shopping Mall"
    cost = 10
    quantity = 1
    public_card = False


class AmusementPark(Card):
    name = "Amusement Park"
    cost = 10
    quantity = 1
    public_card = False


class RadioTower(Card):
    name = "Radio Tower"
    cost = 10
    quantity = 1
    public_card = False


buildings = [Farm(), Ranch(), Bakery(), Cafe(), ConvenienceStore()]


class Player():
    def __init__(self, strat=1):
        self.money = 4
        self.my_b = []
        self.strat = strat
        self.landmarks = {"Station": False, "Shopping Mall": False, "Amusement Park": False, "Radio Tower": False}

    def has_won(self):
        print(self.landmarks)
        print(not False in self.landmarks.values())
        return not False in self.landmarks.values()

    def get_reward(self, roll, is_turn):
        print(roll, 'is roll')
        for b in self.my_b:
            if b:
                reward = b.check(roll, is_turn)
                if reward:
                    print(reward, 'is reward')
                    self.money += reward
        return self.money

    def cafe_steal(self):
        pass

    def choose_buy(self):
        if self.strat == 0:
            print(get_remain())
            print(self.money)
            print(self.my_b)
            choice = input("choose a building")

            a = int(choice)
            building = buildings[a].buy()
            print("Human built ", building.name)
            self.my_b.append(building)

        if self.strat == 1:
            if self.money >= 1:
                self.my_b.append(buildings[1].buy())
                print('Strat 1 built a ranch')
        if self.strat == 2:
            if self.money >= 2:
                self.my_b.append(buildings[4].buy())
                print('Strat 2 built a convenience store')

    def tv_steal(self):
        pass

    def business_center(self):
        pass

    def roll2(self):
        return False

    def reroll(self, total, doubles = False):
        return True


def get_remain():
    return [b.quantity for b in buildings]


def roll1():
    return random.randrange(5) + 1


def roll2():
    a = roll1()
    b = roll1()
    return [a + b, a == b]


class Game():
    def __init__(self, players=None):
        if players:
            self.players = players
        else:
            self.players = [Player(0), Player(1), Player(2)]

        curr_player = 0

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
        if p.landmarks['Station']:
            if p.roll2():
                rolls = roll2()
                roll = rolls[0]
                doubles = rolls[1]
            else:
                roll = roll1()
        else:
            roll = roll1()
        if not used_radio and p.landmarks["Radio Tower"] and p.reroll(roll,doubles):
            return self.roll(p,True)
        else:
            self.give_rewards(roll, p)
            return doubles

    def give_rewards(self, roll, player):
        for p in self.players:
            p.get_reward(roll, p == player)

game = Game()
game.play_game()
print("Done")


# players = [Player(0), Player(1), Player(2)]
# for i in range(5):
#     for player in players:
#         roll = roll1()
#         for player2 in players:
#             player2.get_reward(roll, player == player2)
#         player.choose_buy()
#
# for player in players:
#     print(player.money)
