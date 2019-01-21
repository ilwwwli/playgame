#Todo:增加简单界面，交互操作
from time import sleep

import pygame
import sys
from common import Setting,State
from world import World
from role import Motion
from map import Map
from pyUI import PyUI

def new_start(setting,screen):
    ui = PyUI(setting)
    world = World(setting)
    while world.state.time < 3:
        while True:
            world.should_add_time = 0
            ui.wait_op(screen,world,setting)
            command_str = ''
            if world.me.motion != Motion.NOTHING:
                continue
            if world.me.directing: #若主角指令非空
                command_str = world.me.directing.pop()
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
            elif command[0] == 'find_way':
                tar = (int(command[1]),int(command[2]))
                rs = world.me.find_way((world.me.posx,world.me.posy),tar,world.map)
            elif command[0] == 'move':
                direction = int(command[1])
                rs = world.me.move(direction,world)
            if rs == False:
                continue
            #if rs:
                #ui.action(command,screen,world,setting)#播放动画
            if world.should_add_time:
                print('现在时间:%d年%d月%d日'%(world.state.get_year(),world.state.get_month(),world.state.get_day()))
                world.state.day_add()
    print('剧终')

def main():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.window_width, setting.window_height))
    pygame.display.set_caption("game")
    new_start(setting,screen)

main()