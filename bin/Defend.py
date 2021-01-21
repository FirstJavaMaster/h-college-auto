import time

from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb


class Defend:
    adb = AutoAdb()

    def run(self):
        self.adb.wait('images/defend/open-page.png').click()

        award_num = 0
        while True:
            take_award = self.adb.wait('images/defend/take-award.png', max_wait_time=3).click()
            if not take_award:
                print('已经没有驻守奖励')
                break
            self.adb.wait('images/defend/take-award-confirm.png').click()
            award_num = award_num + 1
            print('驻守奖励 + %d' % award_num)

        started_num = 0
        swiped_num = 0
        while True:
            started = self.adb.wait('images/defend/start.png', max_wait_time=2).click()
            if started:
                started_num = started_num + 1
                self.adb.wait('images/defend/pick-people.png').click()
                self.adb.wait('images/defend/start-confirm.png').click()
                print('开始驻守 + %d' % started_num)
                continue
            if swiped_num >= 4:
                print('应该没有待驻守任务了, 结束')
                PageHelper().back()
                break
            self.adb.swipe(400, 1400, 400, 600)
            time.sleep(1)
            swiped_num = swiped_num + 1


if __name__ == '__main__':
    Defend().run()
