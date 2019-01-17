from common import Setting,State
from map import Map
from role import Role

class World(object):
    def __init__(self,setting):#世界的生成，主角初始化
        self.map = Map(setting.map_width,setting.map_height)
        self.state = State(setting)
        self.me =  Role(1,1,'猪脚')
        self.me.setting_attr(1,1000)
        self.me.check()
