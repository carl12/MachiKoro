import Cards
import GameState

class Player:
    def __init__(self, game, strat=1, name = None):
        self.game = game
        self.money = 4
        self.my_b = []
        self.strat = strat

        self.name = name if name else str(strat)
        self.landmarks = [Cards.Station(), Cards.ShoppingMall(), Cards.AmusementPark(), Cards.RadioTower()]


    def has_won(self):
        return not False in [a.owned for a in self.landmarks]

    def get_reward(self, roll, is_turn, turn_state):
        bonuses = {"Shopping Mall": self.landmarks[1].owned}
        for b in self.my_b:
            if b:
                turn_state.card = b.name
                reward = b.check(roll, is_turn, bonuses)
                if reward:
                    print('Player:',self.name,'just got',reward)
                    self.money += reward
                turn_state.card = None
        return self.money

    def buy(self, num):
        if num < 0:
            num = -num + -1
            if not self.landmarks[num].owned and self.money >= self.landmarks[num].cost:
                pending = self.landmarks[num]
                self.money -= pending.cost
                return pending.buy()
            return
        pending = self.game.take(num)
        if pending and pending.cost <= self.money:
            self.money -= pending.cost
            return pending

    def print_remain(self):
        for b in self.game.buildList:
            print(b.name,str(b.remain),", ",end="")
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

    def state(self):
        counts = {b.name: self.my_b.count(b) for b in set(self.my_b)}

        # Make sure different objects aren't present in my_b
        return GameState.PlayerState(self.name,(self.strat==0),self.money,counts)


class PlayerState:
    def __init__(self, name, is_human, money, owned):
        self.name = name
        self.is_human = is_human
        self.money = money
        self.owned = owned
