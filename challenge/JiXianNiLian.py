from ClickHelper import ClickHelper
from Team import Team


class JiXianNiLian:

    @staticmethod
    def run():
        ClickHelper.click(135, 630)
        ClickHelper.click(270, 890)
        Team.send_team()
