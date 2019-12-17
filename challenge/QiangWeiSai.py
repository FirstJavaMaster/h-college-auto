from ClickHelper import ClickHelper
from Team import Team


class QiangWeiSai:

    @staticmethod
    def run():
        print('进入抢位赛')
        ClickHelper.click(240, 450, wait_second=1)

        refresh_count = 0
        while True:
            if ClickHelper.exist('src/challenge/qiang-wei-sai/none-chance.png', confidence=0.99):
                print('次数已经用完, 退出抢位赛')
                ClickHelper.try_return()
                break

            if ClickHelper.exist('src/challenge/qiang-wei-sai/none-person.png', confidence=0.6):
                print('找到放水队伍, 开始挑战')
                ClickHelper.click_pic('src/challenge/qiang-wei-sai/none-person.png', confidence=0.6)
                Team.wait_fighting_finish()
            else:
                if refresh_count >= 20:
                    print('长时间未找到放水队伍, 不再刷新, 退出')
                    ClickHelper.try_return()
                    break
                refresh_count = refresh_count + 1
                print('未找到放水队伍, 刷新第%d次...' % refresh_count)
                ClickHelper.click(530, 625)
