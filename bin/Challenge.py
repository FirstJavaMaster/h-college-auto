from bin.challenge.BattleDrill import BattleDrill
from bin.challenge.GoodPrepare import GoodPrepare
from bin.PageHelper import PageHelper
from commons.AutoAdb import AutoAdb


class Challenge:
    adb = AutoAdb()

    def run(self):
        to_page = PageHelper().go_to_challenge_page()
        if not to_page:
            return
        # 物资筹备
        GoodPrepare().run()
        # 对战演习
        BattleDrill().run()


if __name__ == '__main__':
    Challenge().run()
