import os
from configparser import ConfigParser

from commons import PathUtils
from commons.Singleton import Singleton


# 配置类, 在ini配置文件里的所有配置项在这里都会有对应的获取方法
class Config:
    # 设备地址
    @staticmethod
    def device_location():
        return get('device_location')

    # pick_flag 配置
    class PickFlag:
        # "物资筹备"中"元素收集"的范围
        @staticmethod
        def good_prepare_item():
            return get('good_prepare_item', 'pick_flag', '1,1,1,1,1')

        # "物资筹备"中"职业考核"的范围
        @staticmethod
        def good_prepare_work():
            return get('good_prepare_work', 'pick_flag', '1,1,1')


# 读取配置文件
def get(key, section='default', fallback=None):
    cp = ConfigParserHolder().get()
    return cp.get(section, key, fallback=fallback)


# 单例模式. 配置文件只读一次
@Singleton
class ConfigParserHolder:
    _cp = ConfigParser()

    def __init__(self):
        # 读取配置文件
        config_file = PathUtils.get_work_dir() + '/config.ini'
        if not os.path.isfile(config_file):
            print('配置文件 config.ini 不存在，请将程序根目录的 config_temp.ini 文件拷贝一份并命名为 config.ini。注意要自行调整其中的配置项。')
            exit(1)
        if not os.access(config_file, os.R_OK):
            print('配置文件 config.ini 不可读，请将程序根目录的 config_temp.ini 文件拷贝一份并命名为 config.ini。注意要自行调整其中的配置项。')
            exit(1)
        self._cp.read(config_file, encoding='utf-8')

    def get(self):
        return self._cp
