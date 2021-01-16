import time

from commons.AutoAdb import AutoAdb
from commons.Timer import Timer


class FightHelper:
    adb = AutoAdb()

    def fight(self):
        print('正在进入战斗 ... ')
        confirmed = self.adb.wait('images/fight/confirm.png', 'images/fight/confirm-1.png').click()
        if not confirmed:
            print('战斗进入失败')
            return False

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
            # 如果还没结束就1秒后再等等
            time.sleep(1)
