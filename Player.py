HIT = 0
STICK = 1


class Player(object):
    def __init__(self):
        self.description = "Base player."
        self.number_of_aces_used = 0
        self.current_total = 0

    def new_card_drawn(self, new_card):
        print "Card drawn:", new_card.number, new_card.suit
        self.current_total += new_card.get_value()

        if self.current_total + 10 <= 21 and new_card.get_value() == 1:
            self.current_total += 10
            self.number_of_aces_used += 1

        while self.is_bust() and self.number_of_aces_used > 0:
            self.number_of_aces_used -= 1
            self.current_total -= 10

    def is_bust(self):
        return self.current_total > 21

    def get_current_total(self):
        return self.current_total

    def choose_action(self, state):
        raise NotImplementedError("This player has no brain, and therefore no way to make a choice")

    def receive_reward(self, reward):
        raise NotImplementedError("This player has no brain, and therefore nothing to do with a reward")