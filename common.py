class Setting(object):
    def __init__(self):
        self.window_width = 1024
        self.window_height = 768
        self.start_year = 1600
        self.action_rate = 5 #动作速率
        self.action_frame_num = 20 #每秒动作帧数
        self.refresh_gap = 1000//30#屏幕刷新间隔,分母表示上限帧率


class State(object):
    def __init__(self,setting):
        self.view_x = 0
        self.view_y = 0
        self.time = 1
        self.start_year = setting.start_year

    def get_year(self):
        return self.time // 360 + self.start_year

    def get_month(self):
        return self.time % 360 // 30 + 1

    def get_day(self):
        return self.time % 360 % 30 + 1

    def day_add(self):
        self.time += 1