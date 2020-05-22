# -*- coding:utf-8 -*-
from fight import img, STEP, offlinefind, startfind, selection, gofind, go
from time import sleep


def stage(number):
    '''选关'''
    while True:
        offlinefind(img)
        if startfind(img):
            selection(number)
            break
        sleep(STEP)


def team(number):
    '''选队伍和点击出发'''
    while True:
        offlinefind(img)
        if gofind(img):
            go(number)
            break
        sleep(STEP)


def fight():
    '''选战斗'''
