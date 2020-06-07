# TODO

import numpy as nm
import pytesseract
import pyautogui
import time
import random
import math
import sys
import subprocess

import cv2
import pyscreenshot as ImageGrab


global play_hours
play_hours = 5
global first_time

if len(sys.argv) > 1:
    play_hours = int(sys.argv[1])

bot_start_time = time.time()
global logout_time
logout_time = time.time()

sayings = ["I am become death, destroyer of fleshcrawlers!",
           "Die filthy creature!",
           "My ancestors smile upon me, can you say the same?",
           "Rot in hell vile abomination!",
           "I will have my vengence!",
           "Deus Vult!",
           "I will cleanse the earth of these filthy beings!"]

wait_time = 10
center_x = 560
center_y = 225
enemies = " min wolf gob spi rat"
loot = " coin arr rune tin cop min zom gob "
stuff_to_click = loot
stuff_to_click += enemies

spells = [1040, 250]
lumby_spell = [865,280]
goblin_run = [900,100]

bury_bones_counter = 0

def kill_epiphany():
    subprocess.call(["sudo pkill -9 -f epiphany"], shell=True)

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

def handle_loot_under_cursor(x,y):
    global wait_time
    left_click(x, y)
    time.sleep(wait_time)
    return

def click_mini_map():
    x = 943
    y = 148
    place_cursor(x, y)
    left_click(x,y)

def log_out():
    kill_epiphany()
    time.sleep(3)

    x = 945
    y = 550
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(1)
    
    # If World switcher is active
    x = 1025
    y = 512
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(2)

    # IF world switcher is not active
    x = 950
    y = 500
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(2)


def log_in():
    kill_epiphany()
    time.sleep(3)

    # Sometimes we can't type anything
    # This is a workaround
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

    x = 750
    y = 360
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(3)
    
    login = "preston_stephens@yahoo.com\tmypassword0\n"
    pyautogui.write(login)
    time.sleep(10)
    
    x = 650
    y = 400
    place_cursor(x, y)
    left_click(x,y)

    time.sleep(3)
    pyautogui.keyDown('up')
    time.sleep(5)
    pyautogui.keyUp('up')

    time.sleep(1)
    #point_south()

def point_south():
    time.sleep(3)
    pyautogui.keyDown('right')
    time.sleep(1.75)
    pyautogui.keyUp('right')


def check_drop(times=5):
    feet_x = center_x
    feet_y = center_y+15
    time_between_caps = 0.5

    diff_x = 23
    diff_y = 10
    top_left_x = feet_x - 2*diff_x
    top_left_y = feet_y - 2*diff_y
    near_positions = [[feet_x, feet_y], [feet_x+diff_x, feet_y],[feet_x-diff_x, feet_y],[feet_x, feet_y+diff_y],[feet_x, feet_y-diff_y]]
    for t in range(times):
        # Search near character
        for position in near_positions:
            place_cursor(position[0], position[1])
            if(loot_under_cursor()):
                handle_loot_under_cursor(position[0], position[1])
                return
            time.sleep(time_between_caps)
    
    for t in range(times):
        # Search grid
        for x in range(5):
            for y in range(3):
                if(x == 2 and y == 1):
                    positions = [[feet_x, feet_y-diff_y], [feet_x, feet_y+diff_y]]
                    for pos in positions:
                        place_cursor(pos[0], pos[1])
                        if(loot_under_cursor()):    
                            handle_loot_under_cursor(pos[0], pos[1])
                            return
                pos = [top_left_x + (x*diff_x), top_left_y + (2*y*diff_y)]
                place_cursor(pos[0], pos[1])
                if(loot_under_cursor()):
                    handle_loot_under_cursor(pos[0], pos[1])
                    return
                time.sleep(time_between_caps)
    click_mini_map()

def new_logout_time():
    return time.time() + 60*45
    return time.time() + 3600 + (random.randint(0,100)/100)* 3600*2

def new_reset_time():
    return time.time() + 3*60

def say_stuff():
    string = sayings[random.randint(0,len(sayings)-1)]
    pyautogui.write("/  \n")
    #pyautogui.write('/' + string + "\n")

def reset_flesh_crawlers_2():
    long_time = 10

    x = 1025
    y = 512
    place_cursor(x, y)
    #left_click(x,y)
    time.sleep(long_time*2)


def reset_flesh_crawlers():
    short_time = 3
    long_time = 10
    
    # Go to gate
    x = 940
    y = 200
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time)

    # Open inner gate
    x = 550
    y = 250
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time)
    
    # Open outer gate
    x = 550
    y = 310
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time*2)

    # Run down hallway
    x = 1000
    y = 150
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time)

    # Exit 2nd inner gate
    x = 600
    y = 200
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time)

    # Exit 2nd outer gate
    x = 650
    y = 200
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time*2)

    # Go Up to flesh crawler
    x = 942
    y = 105
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time*2)
    
    keep_alive(seconds=60*10)

    # Go up to gate
    x = 950
    y = 100
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time)

    # Enter Up through gate
    x = 550
    y = 200
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time)

    # Enter up through gate again
    x = 550
    y = 150
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time*2)

    global logout_time
    if(time.time() > logout_time):
        log_out()
        log_in()
        logout_time = new_logout_time()

    # Run to back gate
    x = 900
    y = 125
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time)

     # Open outer gate
    x = 525
    y = 225
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time)

     # Open inner gate
    x = 475
    y = 225
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(short_time*2)

     # Run to position
    x = 925
    y = 200
    place_cursor(x, y)
    left_click(x,y)
    time.sleep(long_time)
    #keep_alive(seconds=10*60)

def keep_alive(seconds=60):
    for x in range(seconds):
        time.sleep(1)
        if(random.randint(0,5) == 1):
            say_stuff()
            click_mini_map()

logout_time = new_logout_time()
while(True):
    time.sleep(3)
    reset_flesh_crawlers()
    print("{} seconds left".format(-(time.time() - bot_start_time) + 60*60*play_hours))
    if time.time() - bot_start_time > 60*60*play_hours: 
        exit(0) 
    
    
