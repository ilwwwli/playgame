class Setting(object):
    def __init__(self):
        self.window_width = 1024
        self.window_height = 768
        self.map_width = 20
        self.map_height = 20
        self.start_year = 1600

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