import time

from commons.AutoAdb import AutoAdb
from commons.Timer import Timer


class FightHelper:
    adb = AutoAdb()

    def fight(self):
        print('正在进入战斗 ... ')
        confirm_list = ['images/fight/confirm.png', 'images/fight/confirm-1.png',
                        'images/fight/confirm-2.png', 'images/fight/confirm-3.png']
        # 只要没见到 认输  按钮, 则说明没进入战斗
        while not self.adb.check('images/fight/fighting.png'):
            self.adb.click(*confirm_list)

        print('\r战斗进行中 ... ', end='')
        timer = Timer()
        finish_list_success = ['images/fight/finish-success.png', 'images/fight/finish-success-next-stage.png']
        finish_list_fail = ['images/fight/finish-fail.png']
        while True:
            print('\r战斗进行中 ... %s ' % timer.get_duration_string(), end='')
            if self.adb.click(*finish_list_success):
                print('战斗结束[成功]\n')
                return True
            if self.adb.click(*finish_list_fail):
                print('战斗结束[失败]\n')
                return False
            if self.adb.check('images/fight/finish.png'):
                self.adb.click_position(600, 1800)
                print('战斗结束\n')
                return True
            # 如果还没结束就1秒后再等等
            time.sleep(1)
