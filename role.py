import enum

class Motion(enum.Enum):
    NOTHING = 0
    MOVING = 30
    DIREC_UP = 1
    DIREC_DOWN = 2
    DIREC_LEFT = 3
    DIREC_RIGHT = 4

class Role(object):
    def __init__(self,posx,posy,name):
        self.posx = posx#地图格子坐标
        self.posy = posy
        self.posx_float = 0#地图绝对浮点坐标
        self.posy_float = 0
        self.name = name
        self.motion = Motion.NOTHING
        self.motion_param = Motion.NOTHING

    def setting_attr(self,rank,money):
        self.rank = rank
        self.money = money

    def update_action(self,map,setting):
        if self.motion == Motion.MOVING:
            if self.motion_param == Motion.DIREC_UP:
                self.posy_float -= map.block_len / setting.action_frame_num * setting.action_rate
                if self.posy_float <= self.posy * map.block_len:
                    self.posy_float = self.posy * map.block_len
                    self.motion = Motion.NOTHING
            elif self.motion_param == Motion.DIREC_DOWN:
                self.posy_float += map.block_len / setting.action_frame_num * setting.action_rate
                if self.posy_float >= self.posy * map.block_len:
                    self.posy_float = self.posy * map.block_len
                    self.motion = Motion.NOTHING
            elif self.motion_param == Motion.DIREC_LEFT:
                self.posx_float -= map.block_len / setting.action_frame_num * setting.action_rate
                if self.posx_float <= self.posx * map.block_len:
                    self.posx_float = self.posx * map.block_len
                    self.motion = Motion.NOTHING
            elif self.motion_param == Motion.DIREC_RIGHT:
                self.posx_float += map.block_len / setting.action_frame_num * setting.action_rate
                if self.posx_float >= self.posx * map.block_len:
                    self.posx_float = self.posx * map.block_len
                    self.motion = Motion.NOTHING

    def move(self,direction,map):#上下左右移动
        if self.motion != Motion.NOTHING:
            return False
        self.motion = Motion.MOVING
        if direction == 1 and self.posy-1>=0 and map.ground[self.posx][self.posy-1] <= 10:#上
            self.posy -= 1
            self.motion_param = Motion.DIREC_UP
        if direction == 2 and self.posy+1<map.map_height and map.ground[self.posx][self.posy+1] <= 10:#下
            self.posy += 1
            self.motion_param = Motion.DIREC_DOWN
        if direction == 3 and self.posx-1>=0 and map.ground[self.posx-1][self.posy] <= 10:#左
            self.posx -= 1
            self.motion_param = Motion.DIREC_LEFT
        if direction == 4 and self.posx+1<map.map_width and map.ground[self.posx+1][self.posy] <= 10:#右
            self.posx += 1
            self.motion_param = Motion.DIREC_RIGHT

    def move_to(self,posx,posy,map):#瞬移，一般作弊模式或调试模式用，某些技能下也可用
        if posx>=0 and posx< map.map_width and posy>=0 and posy < map.map_height:
            self.posx = posx
            self.posy = posy
            self.posx_float = posx * map.block_len
            self.posy_float = posy * map.block_len
            print('移动到%d,%d'%(posx,posy))
            return True
        else:
            print("移动超出范围！")
            return False

    def check(self):
        print('我叫%s，我在位置(%d,%d)，我%d级了,我有%d金币' % (self.name, self.posx, self.posy, self.rank, self.money))