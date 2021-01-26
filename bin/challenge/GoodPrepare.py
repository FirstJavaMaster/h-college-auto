import time

from bin.FightHelper import FightHelper
from bin.PageHelper import PageHelper
from commons import RandomUtils
from commons.AutoAdb import AutoAdb
from commons.Config import Config


class GoodPrepare:
    adb = AutoAdb()

    def run(self):
        print('检查[物资筹备]的挑战机会 ... ')
        things = {
            'good': not self.adb.check('images/challenge/good-prepare/good-none.png', threshold=0.98),
            'item': not self.adb.check('images/challenge/good-prepare/item-none.png', threshold=0.98),
            'work': not self.adb.check('images/challenge/good-prepare/work-none.png', threshold=0.98)
        }

        if True not in things.values():
            print('各挑战机会均已耗尽. 物资筹备结束!')
            return True

        # 进入子页面
        self.adb.click_position(250, 350)
        if things['good']:
            self.do_good()
        if things['item']:
            self.do_item()
        if things['work']:
            self.do_work()
        PageHelper().back()

    def do_good(self):
        print('开始[物资筹备] ... ')
        self.adb.click_position(500, 450)

        while True:
            # 检查机会
            if self.adb.check('images/challenge/good-prepare/challenge-none.png', threshold=0.95):
                print('机会耗尽, 挑战结束!')
                PageHelper().back()
                return True

            # 只做 电池收集
            self.adb.click_position(900, 300)
            # 再次判断有没有机会
            if self.adb.check('images/buy-confirm.png'):
                print('机会耗尽, 挑战结束!')
                PageHelper().back(2)
                return True

            if self.adb.check('images/fight/confirm-1.png'):
                fight_result = FightHelper().fight()
                if not fight_result:
                    print('战斗失败, 中止操作!')
                    return False
            time.sleep(1)

    def do_item(self):
        print('开始[元素收集] ... ')
        self.adb.click_position(500, 900)

        while True:
            # 检查机会
            if self.adb.check('images/challenge/good-prepare/challenge-none.png', threshold=0.95):
                print('机会耗尽, 挑战结束!')
                PageHelper().back()
                return True

            pos_x = 900
            pox_y = RandomUtils.super_choice([300, 600, 900, 1200, 1500], Config.PickFlag.good_prepare_item())
            print('随机选择一项: pos_x:%d, pos_y:%d' % (pos_x, pox_y))
            self.adb.click_position(pos_x, pox_y)

            # 再次判断有没有机会
            if self.adb.check('images/buy-confirm.png'):
                print('机会耗尽, 挑战结束!')
                PageHelper().back(2)
                return True

            if self.adb.check('images/fight/confirm-1.png'):
                fight_result = FightHelper().fight()
                if not fight_result:
                    print('战斗失败, 中止操作!')
                    return False
            time.sleep(1)

    def do_work(self):
        print('开始[职业考核] ... ')
        self.adb.click_position(500, 1400)

        while True:
            # 检查机会
            if self.adb.check('images/challenge/good-prepare/challenge-none.png', threshold=0.95):
                print('机会耗尽, 挑战结束!')
                PageHelper().back()
                return True

            pos_x = 900
            pox_y = RandomUtils.super_choice([300, 600, 900], Config.PickFlag.good_prepare_work())
            print('随机选择一项: pos_x:%d, pos_y:%d' % (pos_x, pox_y))
            self.adb.click_position(pos_x, pox_y)

            # 再次判断有没有机会
            if self.adb.check('images/buy-confirm.png'):
                print('机会耗尽, 挑战结束!')
                PageHelper().back(2)
                return True

            if self.adb.check('images/fight/confirm-1.png'):
                fight_result = FightHelper().fight()
                if not fight_result:
                    print('战斗失败, 中止操作!')
                    return False
            time.sleep(1)


if __name__ == '__main__':
    GoodPrepare().run()
