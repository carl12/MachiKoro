import json

class GameState:
    """
    Game state structure
     - Dict of
        - remain - array of remaining cards
        - turn_state - dict of components of game state
            - player_turn - who's turn
            - stage - 0 rolling, 1 resolving roll, 2 purchasing, 3, 4, 5 (for second turn using amusement park)
            - card - (only for stage 1) which card is being resolved
            - player - which player is making decision about card reward (only for stage 1 when card requires choice)
        - roll - current roll
        - players - array of players info
            - name - string
            - is_human - boolean
            - money - current money
            - cards - dict of number of currently owned cards

    """
    def __init__(self, remain, turn_state, roll, players):
        self.remain = remain
        self.turn_state = turn_state
        self.roll = roll
        self.players = players
        player_data = [p.__dict__ for p in players]
        self.data = {'remain':self.remain,'turn_state':turn_state.__dict__,'roll':roll,'players':player_data}

    def p_has(self, num, card_name):
        return card_name in self.players[num]


    def get_json(self):
        return json.dumps(self.data)


class TurnState:
    def __init__(self, player_turn, stage, card, pending_player):
        self.player_turn = player_turn
        self.stage = stage
        self.card = card
        self.pending_player = pending_player

    def set_pre_roll(self, first_turn = True):
        self.state = 0 if first_turn else 3

    def set_resolving_roll(self,first_turn = True):
        self.state = 1 if first_turn else 4

    def set_buying(self,first_turn = True):
        self.state = 2 if first_turn else 5





class PlayerState:
    def __init__(self, name, is_human, money, owned):
        self.name = name
        self.is_human = is_human
        self.money = money
        self.owned = owned



if __name__ == '__main__':
    a = TurnState(0,0,0,0)
    print(a.__dict__)
    b1 = PlayerState('steve',True,2,{'Convenience Store':1})
    b2 = PlayerState('bob',False,2,{'Convenience Store':1})
    b3 = PlayerState('joe',False,2,{'Convenience Store':1})
    print(b1.__dict__)


    c = GameState([6,6,6,6,5,6],a,3,[b1,b2,b3])
    # print(c.__dict__)

    print(c.data)
    print(c.get_json())

    # state = {'remain':[6,6,6,6],'turn_state':{'player_turn':0,'stage':0,'card':None,'pending_player':2},'roll':0,'players':[{'name':'steve','type':'human','money':3,'cards':{'Convenience Store':6,'Shopping Mall':1}}]}
