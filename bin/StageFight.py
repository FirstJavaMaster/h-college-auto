import time

from bin.FightHelper import FightHelper
from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb
from commons.Timer import Timer


class StageFight:
    adb = AutoAdb()

    def run(self):
        if not PageHelper().go_to_fight_page():
            return

        timer = Timer()
        while True:
            if not self.adb.click('images/stage-fight/fight-boss.png'):
                print('\r寻敌中 ... %s' % timer.get_duration_string(), end='', flush=True)
                time.sleep(1)
                continue

            print('发现boss, 即将开始boss战斗 ... ')
            fight_result = FightHelper().fight()
            if not fight_result:
                print('战斗失败, 重试')
            timer.init()


if __name__ == '__main__':
    StageFight().run()
