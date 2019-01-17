#单独将UI相关操作提取出来以方便语言移植
import sys
import pygame
from pygame import Rect
class PyUI(object):
    def __init__(self):
        self.ground_image=['' for i in range(0,256)]
        self.ground_image[1] = pygame.image.load('resources/grass.bmp')
        self.ground_image[11] = pygame.image.load('resources/mountain1.bmp')
        self.ground_image[255] = pygame.image.load('resources/hero.bmp')
        self.view_moving = 0 #0：静止，1-4上下左右
        self.view_moving_rate = 4

    def pos_transform(self,mapx,mapy,map):#根据视点将绝对坐标转换为屏幕坐标
        len = map.block_len
        posx = -map.view_x+mapx*len
        posy = -map.view_y+mapy*len
        return Rect((posx,posy),(len,len))

    def move_view(self,world,setting):#视角移动
        if self.view_moving == 0:#静止
            return
        elif self.view_moving == 1:#上
            if world.map.view_y > 0 - setting.window_height / 2:
                world.map.view_y -= 1*self.view_moving_rate
        elif self.view_moving == 2:#下
            if world.map.view_y < world.map.map_height*world.map.block_len - setting.window_height / 2:
                world.map.view_y += 1*self.view_moving_rate
        elif self.view_moving == 3:#左
            if world.map.view_x > 0 - setting.window_width / 2:
                world.map.view_x -= 1*self.view_moving_rate
        elif self.view_moving == 4:#右
            if world.map.view_x < world.map.map_width * world.map.block_len - setting.window_width / 2:
                world.map.view_x += 1 * self.view_moving_rate

    def wait_op(self,screen,world,setting):
        command_str = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:#按键处理
                if event.key == pygame.K_RIGHT:
                    self.view_moving = 4
                if event.key == pygame.K_LEFT:
                    self.view_moving = 3
                if event.key == pygame.K_UP:
                    self.view_moving = 1
                if event.key == pygame.K_DOWN:
                    self.view_moving = 2
                if event.key == pygame.K_a:
                    command_str = "move_to %d %d"%(world.me.posx - 1,world.me.posy)
                elif event.key == pygame.K_d:
                    command_str = "move_to %d %d"%(world.me.posx + 1,world.me.posy)
                elif event.key == pygame.K_w:
                    command_str = "move_to %d %d"%(world.me.posx,world.me.posy - 1)
                elif event.key == pygame.K_s:
                    command_str = "move_to %d %d" % (world.me.posx,world.me.posy + 1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.view_moving = 0
        self.move_view(world,setting)
        self.update_screen(screen,world,setting)
        return command_str

    def update_screen(self,screen,world,setting):
        screen.fill((0,0,0))
        bl = world.map.block_len
        x_num = setting.window_width // world.map.block_len + 1
        y_num = setting.window_height // world.map.block_len + 1
        for i in range(world.map.view_x//bl,min(world.map.view_x//bl+x_num,world.map.map_height)):
            for j in range(world.map.view_y//bl,min(world.map.view_y//bl+y_num,world.map.map_width)):
                if i>= 0 and j>= 0:
                    screen.blit(self.ground_image[world.map.ground[i][j]],self.pos_transform(i,j,world.map))
        screen.blit(self.ground_image[255], self.pos_transform(world.me.posx,world.me.posy,world.map))
        pygame.display.flip()

