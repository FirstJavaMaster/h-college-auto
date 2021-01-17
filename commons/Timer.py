from datetime import datetime


class Timer:
    start_time = None

    def __init__(self):
        self.start_time = datetime.now()

    def init(self):
        print('timer ', self.start_time)
        self.start_time = datetime.now()
        print('timer >>> ', self.start_time)

    def get_duration(self):
        return (datetime.now() - self.start_time).seconds

    def get_duration_string(self):
        duration = self.get_duration()
        return '%ds' % duration
