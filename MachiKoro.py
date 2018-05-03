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





class Player:
    def __init__(self, game, strat=1):
        self.game = game
        self.money = 4
        self.my_b = []
        self.strat = strat
        self.landmarks = {"Station": False, "Shopping Mall": False, "Amusement Park": False, "Radio Tower": False}

    def has_won(self):
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

    def buy(self, num):
        pending = self.game.buildList[num]
        if pending:
            pending.buy()
            self.money -= pending.cost
            return pending

    def print_remain(self):
        for b in self.game.buildList:
            print(b.name,str(b.quantity),", ",end="")
        print()
        print(self.landmarks)

    def buy_name(self, name):
        return None

    def cafe_steal(self):
        pass

    def choose_buy(self):
        if self.strat == 0:
            self.print_remain()
            print("You have $"+str(self.money))
            print("Your buildings:",self.my_b)
            choice = input("choose a building")

            a = int(choice)
            building = self.buy(a)
            if building:
                print("Human built ", building.name)
                self.my_b.append(building)
            else:
                print("Nothing bought")

        if self.strat == 1:
            if self.money >= 1:
                build = self.buy(1)
                if build:
                    self.my_b.append(build)
                    print('Strat 1 built a ranch')
        if self.strat == 2:
            if self.money >= 2:
                build = self.buy(4)
                if build:
                    self.my_b.append(build)
                    print('Strat 2 built a Convenience Store')

    def tv_steal(self):
        pass

    def business_center(self):
        pass

    def roll2(self):
        return False

    def reroll(self, total, doubles = False):
        return True






def roll1():
    return random.randrange(5) + 1


def roll2():
    a = roll1()
    b = roll1()
    return [a + b, a == b]


class Game():
    def __init__(self, players=None):
        self.buildList = [Farm(), Ranch(), Bakery(), Cafe(), ConvenienceStore()]
        self.buildDict = {b.name:b for b in self.buildList}
        if players:
            self.players = players
        else:
            self.players = [Player(self, 0), Player(self, 1), Player(self, 2)]


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

    def get_remain(self):
        return [b.quantity for b in self.buildList]

    def get_name_remain(self):
        return [b.name+" "+str(b.quantity) for b in self.buildList]

game = Game()
game.play_game()
print("Done")

