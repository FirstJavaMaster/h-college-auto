from ClickHelper import ClickHelper
from Team import Team
from challenge.FightingCountHelper import FightingCountHelper


class ZhiYeKaoHe:

    @staticmethod
    def run():
        print('开始职业考核')
        ClickHelper.click(460, 850)

        while True:
            chance_count = FightingCountHelper.get_chance_number()
            if chance_count == 3:
                print('第1场战斗...')
                ClickHelper.click(470, 230)
            elif chance_count == 2:
                print('第2场战斗...')
                ClickHelper.click(470, 380)
            elif chance_count == 1:
                print('第3场战斗...')
                ClickHelper.click(470, 530)
            else:
                print('挑战次数已用完, 退出')
                ClickHelper.try_return()
                break

            print('开始挑战')
            ClickHelper.click(270, 790)
            Team.send_team()
