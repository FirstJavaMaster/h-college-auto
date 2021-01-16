from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb
from commons.Timer import Timer


class FightStage:
    adb = AutoAdb()

    def run(self):
        if not PageHelper().go_to_fight_page():
            return

        timer = Timer()
        while True:
            if self.adb.click('images/stage-fight/fight-boss.png'):
                break
            print('\r寻敌中 ... %ds' % timer.get_duration(), end='', flush=True)

        self.adb.wait('images/fight/confirm.png').click()
        self.adb.wait('images/fight/finish-success.png', 'images/fight/finish-success-next-stage.png').click()


if __name__ == '__main__':
    while True:
        FightStage().run()
