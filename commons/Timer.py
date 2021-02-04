import datetime
import time


class Timer:
    start_time = None

    def __init__(self):
        self.start_time = datetime.datetime.now()

    def init(self):
        print('timer ', self.start_time)
        self.start_time = datetime.datetime.now()
        print('timer >>> ', self.start_time)

    def get_duration(self):
        return (datetime.datetime.now() - self.start_time).seconds

    def get_duration_string(self):
        duration = self.get_duration()
        return '%ds' % duration

    # 倒计时
    @staticmethod
    def countdown(seconds, alert_template='倒计时 %s ...'):
        the_rest_of_seconds = seconds
        countdown_end_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        while the_rest_of_seconds > 0 and datetime.datetime.now() < countdown_end_time:
            print(('\r' + alert_template) % (str(the_rest_of_seconds) + 's'), end='', flush=True)
            time.sleep(1)
            the_rest_of_seconds -= 1
        print('\r倒计时 (%ss) 结束 √' % seconds)


if __name__ == '__main__':
    Timer.countdown(5)
