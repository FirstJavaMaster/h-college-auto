from ClickHelper import ClickHelper
from Team import Team


class JiFenSai:
    @staticmethod
    def run():
        print('进入积分赛')
        ClickHelper.click(370, 280, 1)

        while True:
            if ClickHelper.exist('src/challenge/ji-fen-sai/fighting-finish.png', confidence=0.99):
                print('本页已全部挑战完毕, 尝试刷新')
                refreshed = JiFenSai.refresh()
                if not refreshed:
                    JiFenSai.receive_award()
                    ClickHelper.try_return()
                    break

            # 挨个挑战
            if ClickHelper.exist('src/challenge/ji-fen-sai/fighting.png'):
                print('开始战斗')
                ClickHelper.click_pic('src/challenge/ji-fen-sai/fighting.png')
                ClickHelper.click_pic('src/challenge/ji-fen-sai/fighting-confirm.png')
                Team.send_team()
            else:
                # 翻页
                ClickHelper.scroll(290, 750, -2000)

    @staticmethod
    def receive_award():
        # 领取奖励
        if not ClickHelper.exist('src/challenge/ji-fen-sai/award-1-r.png'):
            ClickHelper.click(175, 440)
            ClickHelper.try_return('center')
        if not ClickHelper.exist('src/challenge/ji-fen-sai/award-2-r.png'):
            ClickHelper.click(250, 440)
            ClickHelper.try_return('center')
        if not ClickHelper.exist('src/challenge/ji-fen-sai/award-3-r.png'):
            ClickHelper.click(330, 440)
            ClickHelper.try_return('center')
        print('奖励已全部领取')

    @staticmethod
    def refresh():
        if ClickHelper.exist('src/challenge/ji-fen-sai/fresh-none.png', confidence=0.98):
            print('没有刷新次数了')
            return False

        print('刷新队伍')
        ClickHelper.click(485, 990)  # 点击刷新
        ClickHelper.click(275, 635)  # 点击确认
        return True
