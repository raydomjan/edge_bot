#!/usr/bin/env python 
import pyautogui as p
import time
import random


#Function that opens the edge search bar and enters the query provided
#Takes one input : a string of what is to be searched for in edge
def search(query):
    p.hotkey("ctrl","e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.70)



#Function that searches for an image and, depending on the input provided, will click or double click on it
#takes four inputs: the file name of the image(string), whether the image is in grayscale or not(boolean), whether the image should be double clicked or not(boolean)
#, and the degree of confidence the image should be searched with (int 0 - 1.0)
def imageFind(image,g,double,conf):
    a = 0
    b = 0
    while(a==0 and b==0):
        try:
            a,b = p.locateCenterOnScreen(image,confidence = conf ,grayscale=g)
        except TypeError:
            pass

    if double == True:
        p.doubleClick(a,b)
    else:
        p.click(a,b)

    return a,b


count = 0

p.hotkey("win","d")
imageFind("Edge.JPG",False,True,.65)
time.sleep(3)
while count < 2:

   
    p.hotkey("win","up")
    search("bing")
    time.sleep(2)

    searchOps = "qwertyuiopasdfghjklzxcvbnm1234567890!\"£$%^&*()/-+.|¬`[];'#,/{}:@~<>?"
    searchQ = ""

    for z in range(45):
        searchQ += searchOps[random.randint(0,len(searchOps)-1)]

    for y in range(len(searchQ)):
        search(searchQ[:y])



    # Other dashboard rewards



    def locate_img(image): 
        thing2find = p.locateOnScreen(image,confidence = .90) 
        if thing2find == None: 
            return False 
        else: 
            return True




    #mobile searches
        
    time.sleep(2)
    p.hotkey('ctrl',"shift","c")

    p.hotkey("win","up")
    search("bing")
    time.sleep(5)
    searchQ = ""

    for z in range(30):
        searchQ += searchOps[random.randint(0,len(searchOps)-1)]

    for y in range(len(searchQ)):
        search(searchQ[:y])

    time.sleep(2)

    



    # change profile

    if locate_img("harry.JPG"):
        time.sleep(2)
        imageFind("harry.JPG",False,False,.60)
        time.sleep(2)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("enter")
        time.sleep(1)

        
        
    elif locate_img("ray.JPG"):
        time.sleep(2)
        imageFind("ray.JPG",False,False,.50)
        time.sleep(2)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("tab")
        time.sleep(.5)
        p.hotkey("enter")
        time.sleep(1)

    
    count +=1

p.hotkey("ctrl","shift","w")




