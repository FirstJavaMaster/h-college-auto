from ClickHelper import ClickHelper


class FightingCountHelper:
    @staticmethod
    def get_chance_number():
        confidence = 0.99
        if ClickHelper.exist('src/challenge/chance-0.png', confidence=confidence):
            return 0
        elif ClickHelper.exist('src/challenge/chance-1.png', confidence=confidence):
            return 1
        elif ClickHelper.exist('src/challenge/chance-2.png', confidence=confidence):
            return 2
        elif ClickHelper.exist('src/challenge/chance-3.png', confidence=confidence):
            return 3
        else:
            return 0
