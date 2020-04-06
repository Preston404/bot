import numpy as nm
import pytesseract
import win32api, win32con
import time
import random
import math

import cv2
from PIL import ImageGrab

center_x = 640
center_y = 360
pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract.exe'
stuff_to_take = "Coin rune"
should_click_actions = "Attack Take"

def get_custom_cap(x1,y1,x2,y2):
    return ImageGrab.grab(bbox =(x1, y1, x2, y2))

def get_cursor_status_cap():
    #return ImageGrab.grab(bbox =(0, 35, 50, 65))
    return ImageGrab.grab(bbox =(0, 35, 200, 65))

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
    win32api.SetCursorPos((x,y))    
    
def should_click():
    cap = get_cursor_status_cap()
    string = get_color_string_from_cap(cap)
    for word in should_click_actions.split():
        if word in string:
            print(string)
            return True
    if (len(string) > 0):
        print(string)
    return False

def handle_drop_down():
    x_orig, y_orig = win32api.GetCursorPos()
    x, y = x_orig*1.5, y_orig*1.5
    time.sleep(3)
    y_offset = 25
    cap = get_custom_cap(x-125,y+y_offset, x+100,y+y_offset+27)
    string = get_string_from_cap(cap)
    print("found {}".format(string))
    take = False
    if "Take" in string:
        for stuff in stuff_to_take.split():
            if stuff in string:
                take = True
    if ("Att" in string) or ("Goblin" in string) or ("spider" in string) or (take == True):
        print("clicking")
        x = x_orig
        y = int(y_orig + (37/1.5))
        travel_cursor(x, y)
        time.sleep(.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def travel_cursor(x,y):
    current_x, current_y = win32api.GetCursorPos()
    dy = y - current_y
    dx = x - current_x
    steps = 10
    for step in range(1,int(steps)):
        next_x = current_x + int(float(dx*(step/steps))) + random.randint(0,3)
        next_y = current_y + int(float(dy*(step/steps))) + random.randint(0,3)
        ret = place_cursor(next_x, next_y)
        

def enemy_found():
    # Search in spiral pattern
    travel_cursor(center_x,center_y)
    degrees_init = random.randint(0,360);
    degrees = degrees_init
    magnitude = 50
    for i in range(300):
        next_x = center_x + (magnitude * math.cos(degrees*(3.14159/180)))*2
        if degrees > 180:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))*.5
        else:
            next_y = center_y + (magnitude * math.sin(degrees*(3.14159/180)))
        degrees =  (degrees + 10) % 360
        if degrees == degrees_init:
            magnitude += 50
        travel_cursor(next_x, next_y)
        if (should_click()):
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,int(next_x),int(next_y),0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,int(next_x),int(next_y),0,0)
            handle_drop_down()
            return True


while(True):
    attacking = enemy_found()
    if(attacking):
        time.sleep(5)
    
start = time.time()
#handle_drop_down()
print(time.time() - start)
    