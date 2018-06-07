import Cards
import GameState

inputs = ['roll', 'player', 'buy']

requests = ['roll1-2','re-roll','steal','buy']

class GameStep:
    def __init__(self, game_state, input=None):
        assert isinstance(game_state, GameState.GameState)
        self.game_state = game_state
        self.turn_state = game_state.turn_state
        self.input = input

    def next_stage(self):
        curr_stage = self.turn_state.stage
        self.turn_state.stage += 1

    def player_turn_is_ai(self):
        self.game_state.players[self.turn_state.player_turn].is_human
        return





    def step_game_state(self, input):
        p_turn = self.turn_state.player_turn
        turn_stage = self.turn_state.stage
        request = ''
        if self.turn_state.stage in [0,3]:
            self.game_state.roll = self.input['roll']
            if self.turn_state.card is None and self.game_state.p_has(p_turn,"Amusement Park"):
                self.turn_state.card = 'Amusement Park'
                request = 're-roll'
                return self.game_state, request
            else:
                self.next_stage()
        if self.turn_state.stage == [1,4]:

            if self.turn_state.card is None:
                #give out rewards
                roll_sum = sum(self.game_state.roll)
                triggered = Cards.triggers[roll_sum]
                # for each triggered card
                for name in triggered:
                    card = Cards.card_dict[name]()
                    # Check if players have said card
                    for p in self.game_state.players:
                        if name in p.owned.keys():
                            if not card.is_interactive:
                                # If card does not require input collect rewards
                                quantity = p.owned[name]
                                p.money += quantity * card.reward
                            else:
                                # Otherwise send request to human or ask ai
                                if p.is_human:
                                    self.turn_state.stage = 1
                                    self.turn_state.card = name
                                    pending = self.game_state.players.index(p)
                                    self.turn_state.pending_player = pending
                                else:
                                    pass
                                    # ai picks person to steal from
            else:
                pass
                # resume above process from card where left off

            # return if on human player here because we need to ask for buy

        if self.turn_state in [2,5]:
            # make sure input is a valid buy
            # Make sure player has enough money
            # Give player card and reduce card supply
            # Check win condition
            # Check amusement park condition for play agiain
            # Otherwise start next player's turn


    def roll_stage(self, input):
        self.game_state.roll = self.input['roll']
        if self.turn_state.card is None and self.game_state.p_has(p_turn, "Amusement Park"):
            self.turn_state.card = 'Amusement Park'
            request = 're-roll'
            return self.game_state, request
        else:
            self.next_stage()

    def reward_stage(self):
        if self.turn_state.card is None:
            # give out rewards
            roll_sum = sum(self.game_state.roll)
            triggered = Cards.triggers[roll_sum]
            # for each triggered card
            for name in triggered:
                card = Cards.card_dict[name]()
                # Check if players have said card
                for p in self.game_state.players:
                    if name in p.owned.keys():
                        if not card.is_interactive:
                            # If card does not require input collect rewards
                            quantity = p.owned[name]
                            p.money += quantity * card.reward
                        else:
                            # Otherwise send request to human or ask ai
                            if p.is_human:
                                self.turn_state.stage = 1
                                self.turn_state.card = name
                                pending = self.game_state.players.index(p)
                                self.turn_state.pending_player = pending
                            else:
                                pass
                                # ai picks person to steal from
        else:
            pass
            # resume above process from card where left off

            # return if on human player here because we need to ask for buy
        self.next_stage()

    def buy_stage(self):
        pass

    def roll(self, input):

        pass
