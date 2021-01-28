import time

from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb
from commons.Timer import Timer


class FightHelper:
    adb = AutoAdb()

    def fight(self):
        print('正在进入战斗 ... ')
        confirm_list = ['images/fight/confirm.png', 'images/fight/confirm-1.png',
                        'images/fight/confirm-2.png', 'images/fight/confirm-3.png']
        # 判断有没有进入战斗
        while True:
            if self.adb.click(*confirm_list):
                continue
            if self.adb.check('images/fight/fighting.png', 'images/fight/fighting-1.png', new_screenshot=False):
                break

        # 进入战斗后则一直监听战斗结果的若干标记, 否则认为战斗仍在继续
        finish_list_success = ['images/fight/finish-success.png']
        finish_list_fail = ['images/fight/finish-fail.png', 'images/fight/finish-fail-1.png']
        finish_list = ['images/fight/finish.png']

        timer = Timer()
        finish_result = True
        while True:
            print('\r战斗进行中 ... %s ' % timer.get_duration_string(), end='')
            if self.adb.check(*finish_list_success, new_screenshot=True):
                break
            if self.adb.check(*finish_list_fail, new_screenshot=False):
                finish_result = False
                break
            if self.adb.check(*finish_list, new_screenshot=False):
                break
            # 如果还没结束就1秒后再等等
            time.sleep(1)

        print('\n战斗结束[%s]\n' % ('成功' if finish_result else '失败'))
        if not self.adb.click('images/fight/finish-next-stage.png', new_screenshot=False):
            PageHelper().back()
        return finish_result


if __name__ == '__main__':
    FightHelper().fight()
