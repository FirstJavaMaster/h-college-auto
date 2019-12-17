from ChangeMainMenu import ChangeMainMenu, MainMenu
from ClickHelper import ClickHelper
from challenge.JiFenSai import JiFenSai
from challenge.JiXianNiLian import JiXianNiLian
from challenge.QiangWeiSai import QiangWeiSai
from challenge.WuZiChouBei import WuZiChouBei
from challenge.YuanSuSouJi import YuanSuSouJi
from challenge.ZhiYeKaoHe import ZhiYeKaoHe


class Challenge:
    @staticmethod
    def run():
        # 切换到战斗页
        ChangeMainMenu.switch(MainMenu.Fighting)
        # 切换到挑战页
        ClickHelper.click_pic('src/challenge/challenge.png', 'src/challenge/challenge-already.png')

        # 开始积分赛
        JiFenSai.run()

        # 开始抢位赛
        QiangWeiSai.run()

        # 开始极限拟练
        JiXianNiLian.run()

        # 开始物资筹备
        WuZiChouBei.run()

        # 开始元素搜集
        YuanSuSouJi.run()

        # 开始职业考核
        ZhiYeKaoHe.run()
