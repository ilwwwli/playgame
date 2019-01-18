#Todo:增加简单界面，交互操作
from time import sleep

import pygame
import sys
from common import Setting,State
from world import World
from role import Role
from map import Map
from pyUI import PyUI

def new_start(setting,screen):
    ui = PyUI(setting)
    world = World(setting)
    while world.state.time < 3:
        while True:
            command_str = ui.wait_op(screen,world,setting)
            if command_str == '':
                continue
            command = command_str.split()
            print(command)
            if command[0]=='exit':
                sys.exit()
            elif command[0]=='move_to':
                tar_x = int(command[1])
                tar_y = int(command[2])
                rs = world.me.move_to(tar_x,tar_y,world.map)
                if rs==False:
                    continue
            elif command[0] == 'move':
                direction = int(command[1])
                rs = world.me.move(direction,world.map)
            #if rs:
                #ui.action(command,screen,world,setting)#播放动画
            print('现在时间:%d年%d月%d日'%(world.state.GetYear(),world.state.GetMonth(),world.state.GetDay()))
            world.state.dayAdd()
    print('剧终')

def main():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.window_width, setting.window_height))
    pygame.display.set_caption("game")
    new_start(setting,screen)

main()