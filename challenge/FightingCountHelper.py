from ClickHelper import ClickHelper


class FightingCountHelper:
    @staticmethod
    def get_chance_number():
        if ClickHelper.exist('src/challenge/chance-0.png', confidence=0.95):
            return 0
        elif ClickHelper.exist('src/challenge/chance-3.png', confidence=0.95):
            return 3
        else:
            return 0
