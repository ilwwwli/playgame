class Role(object):
    def __init__(self,posx,posy,name):
        self.posx = posx
        self.posy = posy
        self.name = name

    def setting_attr(self,rank,money):
        self.rank = rank
        self.money = money

    def move_to(self,posx,posy,map):
        if posx>=0 and posx< map.map_width and posy>=0 and posy < map.map_height:
            self.posx = posx
            self.posy = posy
            print('移动到%d,%d'%(posx,posy))
            return True
        else:
            print("移动超出范围！")
            return False


    def check(self):
        print('我叫%s，我在位置(%d,%d)，我%d级了,我有%d金币' % (self.name, self.posx, self.posy, self.rank, self.money))