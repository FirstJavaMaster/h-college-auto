import datetime

from ClickHelper import ClickHelper
from Team import Team
from challenge.FightingCountHelper import FightingCountHelper


class YuanSuSouJi:

    @staticmethod
    def run():
        # 进入主界面
        print('开始元素搜集')
        ClickHelper.click(270, 850, wait_second=1)

        position_list = [
            {'x': 470, 'y': 230},
            {'x': 470, 'y': 380},
            {'x': 470, 'y': 530},
            {'x': 470, 'y': 690},
            {'x': 470, 'y': 835}
        ]

        day = datetime.date.today().strftime('%d')
        index_list = [0, 1, 2] if int(day) % 2 == 1 else [1, 3, 4]

        while True:
            chance_number = FightingCountHelper.get_chance_number()
            if chance_number == 3:
                index = index_list[0]
            elif chance_number == 2:
                index = index_list[1]
            elif chance_number == 1:
                index = index_list[2]
            else:
                print('挑战次数已用完, 退出')
                ClickHelper.try_return()
                break

            print('开始挑战')
            position = position_list[index]
            ClickHelper.click(position['x'], position['y'])
            ClickHelper.click(270, 790)
            Team.send_team()
