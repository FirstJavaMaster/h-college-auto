from bin.challenge.BattleDrill import BattleDrill
from bin.challenge.GoodPrepare import GoodPrepare
from commons.AutoAdb import AutoAdb


class Challenge:
    adb = AutoAdb()

    def run(self):
        # 物资筹备
        GoodPrepare().run()
        # 对战演习
        BattleDrill().run()


if __name__ == '__main__':
    Challenge().run()
