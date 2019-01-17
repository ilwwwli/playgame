class Map(object):
    def __init__(self,map_width,map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.block_len = 30#每小块地图边长
        self.view_x=0
        self.view_y=0
        self.ground = [[1 for i in range(map_width)] for j in range(map_height)]
        self.ground[0][0] = 11
        self.ground[map_width-1][0] = 11
        self.ground[map_width-1][map_height-1] = 11
        self.ground[0][map_height-1] = 11

    def read_map(self,filename):
        pass