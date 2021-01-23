from bin.FightHelper import FightHelper
from commons.AutoAdb import AutoAdb


class GoUp:
    adb = AutoAdb()

    def run(self):
        up_num = 0
        while True:
            self.adb.wait('images/go-up/challenge.png').click()
            fight_result = FightHelper().fight()
            if fight_result:
                up_num = up_num + 1
                print('上升 %d 层' % up_num)
                continue
            print('上升失败, 再次尝试')


if __name__ == '__main__':
    GoUp().run()
