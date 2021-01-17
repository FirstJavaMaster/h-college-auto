import time

from bin.FightHelper import FightHelper
from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb


class BattleDrill:
    adb = AutoAdb()

    def run(self):
        print('检查[对战演习]的挑战机会 ... ')
        # things = {
        #     'points': not self.adb.check('images/challenge/good-prepare/good-none.png', threshold=0.95),
        #     'position': not self.adb.check('images/challenge/good-prepare/item-none.png', threshold=0.95),
        #     'team': not self.adb.check('images/challenge/good-prepare/work-none.png', threshold=0.95)
        # }
        #
        # if True not in things.values():
        #     print('各挑战机会均已耗尽. 物资筹备结束!')
        #     return True
        #
        # # 进入子页面
        # self.adb.click_position(250, 750)
        # if things['points']:
        #     self.do_points()
        # if things['position']:
        #     self.do_position()
        # if not things['team']:
        #     self.do_team()
        # PageHelper().back()

        self.adb.click_position(250, 750)
        self.do_points()

    def do_points(self):
        print('开始[积分赛] ... ')
        self.adb.click_position(200, 350)

        while True:
            # 名单中的6个均已挑战成功
            fight_six = self.adb.check('images/challenge/points/six-six.png', threshold=0.95)
            # 如果胜场不到6, 则寻找挑战按钮
            if not fight_six:
                self.do_points_in_unit()
                continue
            print('已经6胜')
            # 如果到6次了, 则看是否还有刷新次数
            none_chance = self.adb.check('images/challenge/points/none-chance.png', threshold=0.95)
            if none_chance:
                print('已经没有刷新次数. 退出[积分赛]!')
                self.do_points_receive_award()
                PageHelper().back()
                return True

            self.adb.wait('images/challenge/points/flush.png').click()
            if self.adb.check('images/challenge/points/flush-confirm-text.png'):
                self.adb.click_position(550, 1050)
                print('次数已刷新. 开启新征程 ...')
                continue
            # 判断是否要付费
            need_money = self.adb.check('images/challenge/points/flush-confirm-text-need-money.png')
            if need_money:
                PageHelper().back()
                print('机会已耗尽. 退出[积分赛]!')
                self.do_points_receive_award()
                PageHelper().back()
                return True

    def do_points_in_unit(self):
        swipe_flag = True
        while not self.adb.click('images/challenge/points/challenge.png'):
            if swipe_flag:
                self.adb.swipe(500, 1700, 500, 1000)
            else:
                self.adb.swipe(500, 1000, 500, 1700)
            # 这里多加一个判断, 如果6胜, 则返回
            if self.adb.check('images/challenge/points/six-six.png'):
                print('已经6胜')
                return True
            swipe_flag = not swipe_flag
            continue
        # 点到 挑战 按钮后, 即开始战斗
        return FightHelper().fight()

    def do_points_receive_award(self):
        nums = 0
        while self.adb.click('images/challenge/points/have_award.png'):
            nums = nums + 1
            print('领取奖励 + %d' % nums)
            PageHelper().back()

    def do_position(self):
        print('开始[抢位赛] ... ')
        pass

    def do_team(self):
        print('开始[团队赛] ... ')
        pass


if __name__ == '__main__':
    BattleDrill().run()
