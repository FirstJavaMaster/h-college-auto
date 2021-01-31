import time

from bin.FightHelper import FightHelper
from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb


class BattleDrill:
    adb = AutoAdb()

    def run(self):
        # 进入 对战演习
        self.adb.click_position(250, 750)
        # 做每个任务
        self.do_points()
        self.do_position()
        self.do_team()
        # 返回
        PageHelper().back()

    def do_points(self):
        print('开始[积分赛] ... ')
        self.adb.click_position(200, 350)

        while True:
            # 名单中的6个均已挑战成功
            fight_six = self.adb.check('images/challenge/points/six-six.png', threshold=0.99)
            # 如果胜场不到6, 则寻找挑战按钮
            if not fight_six:
                self.do_points_in_unit()
                continue
            print('已经6胜')
            # 如果到6次了, 则看是否还有刷新次数
            none_chance = self.adb.check('images/challenge/points/none-chance.png', threshold=0.99)
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
        self.adb.click_position(800, 1000, wait_time=1)

        fight_result = True
        while True:
            # 检查剩余次数
            none_chance = self.adb.check('images/challenge/position/none-chance.png', threshold=0.999)
            if none_chance:
                print('次数耗尽. [抢位赛]结束!')
                PageHelper().back()
                return True
            # 如果战斗失败, 则点击刷新按钮更换对手
            if not fight_result:
                self.adb.wait('images/challenge/position/flush.png').click(1)
            self.adb.click_position(500, 500)
            # 如果未进入战斗, 则可能是"正在被挑战", 继续循环
            if self.adb.wait('images/challenge/position/flush.png', max_wait_time=1).is_valuable():
                print('正在被挑战, 稍等继续...')
                time.sleep(3)
                continue

            # 如果提示购买 则结束抢位赛
            if self.adb.check('images/challenge/position/none-chance-need-money-text.png'):
                PageHelper().back(2)
                return True
            fight_result = FightHelper().fight()
            # 战斗结束后等待一会儿, 让页面动画结束
            time.sleep(1)

    def do_team(self):
        print('开始[团队赛] ... ')
        self.adb.click_position(200, 1600)

        # 点击领取奖励
        self.adb.wait('images/challenge/team/take-award.png').click()
        # 判断是否休赛
        if self.adb.check('images/challenge/team/break-time.png'):
            print('休赛期. 结束[团队赛]!')
            PageHelper().back()
            return True
        # todo 比赛
        pass


if __name__ == '__main__':
    BattleDrill().run()
