import time

from ClickHelper import ClickHelper


class Team:
    @staticmethod
    def send_team(number=1):
        Team.select_team(number)
        # 点击确定按钮
        ClickHelper.click_pic('src/send-team/send-confirm.png')

        # 监听战斗结束
        Team.wait_fighting_finish()

    @staticmethod
    def select_team(number=1):
        print('选用队伍 ', number)
        time.sleep(1)
        if number == 1:
            if not ClickHelper.exist('src/send-team/team-1-active.png'):
                ClickHelper.click(60, 240)
        else:
            raise RuntimeError('暂不支持其他队伍')

    @staticmethod
    def wait_fighting_finish():
        print('监听战斗中 ###', end='')
        while True:
            time.sleep(0.5)

            success = ClickHelper.exist('src/send-team/fighting-end-success.png')
            fail = ClickHelper.exist('src/send-team/fighting-end-fail.png')
            count = ClickHelper.exist('src/send-team/fighting-end-count.png')
            if success or fail:
                print(' 战斗%s' % ('胜利' if success else '失败'))
                ClickHelper.try_return()
                break
            elif count:
                print(' 战斗结束')
                ClickHelper.try_return()
                break
            else:
                print('###', end='')
