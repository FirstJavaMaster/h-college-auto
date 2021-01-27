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
                swiped_num = 0
                self.adb.wait('images/defend/pick-people.png').click()
                self.adb.wait('images/defend/start-confirm.png').click()
                print('开始驻守 + %d' % started_num)
                continue
            if swiped_num >= 2:
                print('没有待驻守任务了')
                PageHelper().back()
                break
            self.adb.swipe(400, 1400, 400, 600)
            time.sleep(1)
            swiped_num = swiped_num + 1
        # 检查额外奖励
        extra_award_num = 0
        while not self.adb.check('images/defend/extra-award-none.png'):
            # todo 点击固定位置 坐标待确定
            self.adb.click_position(200, 900)
            self.adb.wait('images/defend/extra-award-take-confirm.png').click(1)
            extra_award_num = extra_award_num + 1
            print('额外奖励 + ', extra_award_num)


if __name__ == '__main__':
    Defend().run()
