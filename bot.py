# TODO

import numpy as nm
import pytesseract
import pyautogui
import time
import random
import math

import cv2
import pyscreenshot as ImageGrab

bot_start_time = time.time()

wait_time = 25
center_x = 560
center_y = 225
enemies = " min wolf "
loot = " coin arr rune tin copp min"
stuff_to_click = loot
stuff_to_click += enemies

spells = [1040, 250]
lumby_spell = [865,280]
goblin_run = [900,100]

bury_bones_counter = 0

def get_cursor_status_cap():
    return pyautogui.screenshot(region=(305, 65, 200, 20))
    #return pyautogui.screenshot(region=(305, 65, 100, 20))

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
       
def loot_under_cursor():
    cap = get_cursor_status_cap()
    string = get_color_string_from_cap(cap)
    for word in loot.split():
        if word.lower() in string.lower():
            print(string)
            return True
    if (len(string) > 0):
        print(string)
    return False

def left_click(x,y):
    pyautogui.click(x,y)

def move_down(times=5):
    tmp_x = center_x
    tmp_y = center_y+50
    for x in range(times):
        pyautogui.moveTo(tmp_x, tmp_y,1);
        time.sleep(.1)
        left_click(tmp_x,tmp_y)
        time.sleep(1)

def move_up(times=5):
    tmp_x = center_x
    tmp_y = center_y-30
    for x in range(times):
        pyautogui.moveTo(tmp_x, tmp_y,1);
        time.sleep(.1)
        left_click(tmp_x,tmp_y)
        time.sleep(1)

def move_right(times=5):
    tmp_x = center_x+30
    tmp_y = center_y
    for x in range(times):
        pyautogui.moveTo(tmp_x, tmp_y,1);
        time.sleep(.1)
        left_click(tmp_x,tmp_y)
        time.sleep(1)

def click_inventory(string, clicks=1000):
    inventory_icon = [940, 263.5]
    place_cursor(inventory_icon[0], inventory_icon[1])
    time.sleep(1)
    left_click(inventory_icon[0], inventory_icon[1])
    x1, y1 = 880, 290
    for x in range(4):
        for y in range(7):
            new_x, new_y = x1+(x*40), y1+(y*37.5)
            place_cursor(new_x, new_y)
            time.sleep(1)
            cap = get_cursor_status_cap()
            item_found = get_color_string_from_cap(cap)
            print(item_found.lower())
            if (string.lower() in item_found.lower()):
                left_click(new_x,new_y)
                time.sleep(.5)

def enemy_found():
    global bury_bones_counter
    # Search in spiral pattern
    place_cursor(center_x,center_y)
    degrees_init = random.randint(0,360);
    degrees = degrees_init
    magnitude = 50
    for i in range(75):
        if (i % 50 == 0 and i != 0):
            move_right(times=3)
        #bury_bones_counter = (bury_bones_counter+1)%500
        #if(bury_bones_counter == 450):
        #    click_inventory("bone")
        next_x = center_x + (magnitude * math.cos(degrees*(3.14159/180)))
        if degrees > 180:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))*.5
        else:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))*2
        degrees =  (degrees + 10) % 360
        if degrees == degrees_init:
            magnitude += 25
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

def check_drop():
    feet_x = center_x
    feet_y = center_y+15
    left = [feet_x-23, feet_y]
    right = [feet_x+23, feet_y]
    up = [feet_x, feet_y-10]
    down = [feet_x, feet_y+10]
    positions = [left, right, up, down]
    for pos in positions:
        place_cursor(pos[0], pos[1])
        if(loot_under_cursor()):
            left_click(pos[0], pos[1])
            time.sleep(wait_time)
            check_drop()


time_start = time.time()
start = False
while(True):
    check_drop()
    if time.time() - bot_start_time > 60*60*5: # Shut down the bot after 4 hours
        exit(0)
    attacking = enemy_found()
    if(attacking):
        time.sleep(wait_time)
    if (False and time.time() - time_start > 30*60) or start == True:
        time.sleep(15)
        tele_lumby()
        time.sleep(30)
        run_goblins()
        time_start = time.time()
        start = False
    
    
