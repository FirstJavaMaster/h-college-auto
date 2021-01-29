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
        # 战斗进入阶段
        while True:
            # 有确认按钮 则点击按钮
            if self.adb.click(*confirm_list):
                continue
            # 没有确认按钮则检查是否已经在战斗中了
            if self.adb.check('images/fight/fighting.png', 'images/fight/fighting-1.png', new_screenshot=False):
                break
            # 然后检查是否已经结束了. 有些战斗过程非常快, 可能会很快结束战斗
            if self.__finish_check__(new_screenshot=False) is not None:
                break

        # 已经进入战斗
        timer = Timer()
        while True:
            print('\r战斗进行中 ... %s ' % timer.get_duration_string(), end='', flush=True)
            finish_result = self.__finish_check__()
            if finish_result is None:
                time.sleep(1)
                continue
            print('\n战斗结束[%s]\n' % ('成功' if finish_result else '失败'))
            if not self.adb.click('images/fight/finish-next-stage.png', new_screenshot=False):
                PageHelper().back()
            return finish_result

    # 检查战斗是否已经结束
    # 如果未结束返回None; 如果战斗成功返回True; 如果战斗失败返回False
    #
    # new_screenshot参数用于控制"判断时是否获取最新的截屏"
    # 注: 方法内部存在多次判断, new_screenshot即使被设定为True也只会获取一次最新截屏, 后续判断会重复使用第一次的截图
    def __finish_check__(self, new_screenshot=True):
        finish_list_success = ['images/fight/finish-success.png']
        finish_list_fail = ['images/fight/finish-fail.png', 'images/fight/finish-fail-1.png']
        finish_list = ['images/fight/finish.png']

        if self.adb.check(*finish_list_success, new_screenshot=new_screenshot):
            return True
        if self.adb.check(*finish_list_fail, new_screenshot=False):
            return False
        if self.adb.check(*finish_list, new_screenshot=False):
            return True
        return None


if __name__ == '__main__':
    FightHelper().fight()
