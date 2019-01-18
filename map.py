from pygame.sprite import Group

class Map(object):
    def __init__(self,map_width,map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.block_len = 30#每小块地图边长
        self.block_len_max = 70#每小块最大地图边长
        self.block_len_initial = 30#每小块地图初始边长
        self.block_len_change =10#每次缩放改变的边长
        self.view_x=0
        self.view_y=0
        self.ground = [[1 for i in range(map_height)] for j in range(map_width)]
        self.ground[0][0] = 11
        self.ground[map_width-1][0] = 11
        self.ground[map_width-1][map_height-1] = 11
        self.ground[0][map_height-1] = 11
        self.objs = []

    def pos_transform_stw(self,screen_x,screen_y):#根据屏幕坐标转换为地图坐标，不在地图范围内返回(-1,-1)
        abs_x = (screen_x + self.view_x) // self.block_len
        abs_y = (screen_y + self.view_y) // self.block_len
        if abs_x >= 0 and abs_x < self.map_width and abs_y >= 0 and abs_y < self.map_height:
            return (abs_x,abs_y)
        else:
            return (-1,-1)

    def scale_update(self,method, mouse_pos):#缩放地图后更新地图上元素的浮点坐标
        if method == 1:#放大
            if self.block_len < self.block_len_max:
                self.view_x, self.view_y = self.pos_transform_stw(mouse_pos[0], mouse_pos[1])
                self.block_len += self.block_len_change
                self.view_x = self.view_x * self.block_len - mouse_pos[0] + self.block_len // 2
                self.view_y = self.view_y * self.block_len - mouse_pos[1] + self.block_len // 2
            for obj in self.objs:
                obj.posx_float = obj.posx * self.block_len
                obj.posy_float = obj.posy * self.block_len
        elif method ==2:#缩小
            if self.block_len > self.block_len_change:
                self.view_x, self.view_y = self.pos_transform_stw(mouse_pos[0], mouse_pos[1])
                self.block_len -= self.block_len_change
                self.view_x = self.view_x * self.block_len - mouse_pos[0] + self.block_len // 2
                self.view_y = self.view_y * self.block_len - mouse_pos[1] + self.block_len // 2
            for obj in self.objs:
                obj.posx_float = obj.posx * self.block_len
                obj.posy_float = obj.posy * self.block_len

    def add(self,obj):
        obj.posx_float = obj.posx * self.block_len
        obj.posy_float = obj.posy * self.block_len
        self.objs.append(obj)

    def read_map(self,filename):
        pass

