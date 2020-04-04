import numpy as nm
import pytesseract

import cv2
from PIL import ImageGrab

def get_cursor_status_cap():
    return ImageGrab.grab(bbox =(0, 35, 250, 65))

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

def imToString():
    
  
    # Path of tesseract executable 
    pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    count = 0;
    while(True): 
  
       # ImageGrab-To capture the screen image in a loop.  
       # Bbox used to capture a specific area.        
       #cap = get_cursor_status_cap()
       cap = get_dialog_box_cap()
       #cap = get_hp_cap()
       #cap.show()
    
       # Converted the image to monochrome for it to be easily  
       # read by the OCR and obtained the output String. 
       tesstr = get_color_string_from_cap(cap)
       print(tesstr)
        
# Calling the function 
imToString()
    