# TODO

import numpy as nm
import pytesseract
import pyautogui
import time
import random
import math

import cv2
import pyscreenshot as ImageGrab

center_x = 560
center_y = 225
stuff_to_click = "coin gob giant open"

spells = [1040, 250]
lumby_spell = [865,280]
goblin_run = [900,100]


def get_cursor_status_cap():
    return pyautogui.screenshot(region=(305, 65, 100, 20))

def get_dialog_box_cap():
    return ImageGrab.grab(bbox =(0, 960, 600, 1050))

def get_hp_cap():
    return ImageGrab.grab(bbox =(1610, 125, 1640, 150))

def get_string_from_cap(cap):
    return pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang ='eng')

def get_color_string_from_cap(cap):
    return pytesseract.image_to_string(nm.array(cap), lang ='eng')

def get_digits_from_cap(cap):
    return pytesseract.image_to_string(nm.array(cap), lang ='eng', config='digits')

def place_cursor(x,y):
    pyautogui.moveTo(x,y,0.1)
    
def enemy_under_cursor():
    cap = get_cursor_status_cap()
    string = get_color_string_from_cap(cap)
    for word in stuff_to_click.split():
        if word.lower() in string.lower():
            print(string)
            return True
    if (len(string) > 0):
        print(string)
    return False
       

def left_click(x,y):
    pyautogui.click(x,y)

def move_down():
    tmp_x = center_x
    tmp_y = center_y+50
    for x in range(5):
        pyautogui.moveTo(tmp_x, tmp_y,1);
        time.sleep(.1)
        left_click(tmp_x,tmp_y)
        time.sleep(1)

def enemy_found():
    # Search in spiral pattern
    place_cursor(center_x,center_y)
    degrees_init = random.randint(0,360);
    degrees = degrees_init
    magnitude = 50
    for i in range(300):
        if (random.randint(0,65) == 1):
            move_down()
        next_x = center_x + (magnitude * math.cos(degrees*(3.14159/180)))*2
        if degrees > 180:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))*.5
        else:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))
        degrees =  (degrees + 10) % 360
        if degrees == degrees_init:
            magnitude += 50
        place_cursor(next_x, next_y)
        if (enemy_under_cursor()):
            left_click(next_x,next_y)
            return True

def tele_lumby():
    place_cursor(spells[0], spells[1])
    time.sleep(1)
    left_click(spells[0], spells[1])
    
    time.sleep(1)
    place_cursor(lumby_spell[0], lumby_spell[1])
    time.sleep(1)
    left_click(lumby_spell[0], lumby_spell[1])
    
def run_goblins():
    for x in range(2):
        place_cursor(goblin_run[0], goblin_run[1])
        left_click(goblin_run[0], goblin_run[1])
        time.sleep(45)


time_start = time.time()
start = False
while(True):
    attacking = enemy_found()
    if(attacking):
        time.sleep(5)
    if (time.time() - time_start > 30*60) or start == True:
        time.sleep(15)
        tele_lumby()
        time.sleep(30)
        run_goblins()
        time_start = time.time()
        start = False
    
    
