from ClickHelper import ClickHelper
from Team import Team
from challenge.FightingCountHelper import FightingCountHelper


class WuZiChouBei:

    @staticmethod
    def run():
        # 进入主界面
        print('开始物资筹备')
        ClickHelper.click(100, 850)

        while True:
            chance_number = FightingCountHelper.get_chance_number()
            if chance_number == 0:
                print('挑战次数已用完, 退出')
                ClickHelper.try_return()
                break

            # 点击电池本
            ClickHelper.click(470, 230)
            # 确认考核
            ClickHelper.click(270, 790)
            # 派出队伍
            Team.send_team()
