

class Card:
    trigger = [0]
    on_turn = False
    off_turn = False
    reward = 0
    cost = 0
    remain = 10
    public_card = True

    def buy(self):
        if self.remain > 0:
            self.remain = self.remain - 1
            return self

    def check(self, roll, is_turn, boosts = None):
        if (is_turn and self.on_turn) or (not is_turn and self.off_turn):
            if roll in self.trigger:
                return self.get_reward(boosts)

    def get_reward(self, boosts = None):
        return self.reward

    def __repr__(self):
        return self.name


class Farm(Card):
    name = "Farm"
    trigger = [1]
    on_turn = True
    off_turn = True
    reward = 1
    cost = 1
    remain = 6


class Ranch(Card):
    name = "Ranch"
    trigger = [2]
    on_turn = True
    off_turn = True
    reward = 1
    cost = 1
    remain = 6


class FoodShop(Card):
    shopMBonus = 1
    def get_reward(self, boosts = None):
        if boosts and boosts.get("Shopping Mall"):
            return self.reward + self.shopMBonus
        else: return self.reward


class Bakery(FoodShop):
    name = "Bakery"
    trigger = [2, 3]
    on_turn = True
    off_turn = False
    reward = 1
    cost = 1
    remain = 6


class Cafe(FoodShop):
    name = "Cafe"
    trigger = [3]
    on_turn = False
    off_turn = True
    reward = 1
    cost = 2
    remain = 6



class ConvenienceStore(FoodShop):

    name = "Convenience Store"
    trigger = [4]
    on_turn = True
    off_turn = True
    reward = 3
    cost = 2
    remain = 6

class LandmarkCard(Card):
    owned = False
    def buy(self):
        if self.remain > 0:
            self.remain = self.remain - 1
            self.owned=True
            return self

class Station(LandmarkCard):
    name = "Station"
    cost = 4
    remain = 1
    public_card = False


class ShoppingMall(LandmarkCard):
    name = "Shopping Mall"
    cost = 10
    remain = 1
    public_card = False


class AmusementPark(LandmarkCard):
    name = "Amusement Park"
    cost = 16
    remain = 1
    public_card = False


class RadioTower(LandmarkCard):
    name = "Radio Tower"
    cost = 22
    remain = 1
    public_card = False