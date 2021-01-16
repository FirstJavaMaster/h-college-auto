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
        finish_image_list = ['images/fight/finish-success.png', 'images/fight/finish-success-next-stage.png']
        while True:
            print('\r战斗进行中 ... %s' % timer.get_duration_string(), end='')
            if not self.adb.check(*finish_image_list):
                continue
            print(' 战斗结束\n', flush=True)
            self.adb.wait(*finish_image_list).click()
            return True
