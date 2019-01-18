class Setting(object):
    def __init__(self):
        self.window_width = 1024
        self.window_height = 768
        self.map_width = 100
        self.map_height = 50
        self.start_year = 1600
        self.action_rate = 1 #动作速率
        self.action_frame_num = 20 #每秒动作帧数
        self.refresh_gap = 1000//60#屏幕刷新间隔

class State(object):
    def __init__(self,setting):
        self.view_x = 0
        self.view_y = 0
        self.time = 1
        self.start_year = setting.start_year

    def GetYear(self):
        return self.time // 360 + self.start_year

    def GetMonth(self):
        return self.time % 360 // 30 + 1

    def GetDay(self):
        return self.time % 360 % 30 + 1

    def dayAdd(self):
        self.time += 1