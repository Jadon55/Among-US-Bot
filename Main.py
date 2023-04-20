import pyautogui
import keyboard
import numpy as np
from PIL import ImageGrab
import time

use_button = (1787, 922)
id_card_a = (758, 816)
id_card_b = (525, 412)
id_card_c = (1470, 412)
garbage_up = (1296, 417)
garbage_down = (1269, 893)
download_button = (956, 654)
navigation_center = (961, 540)
shield_tiles = [(790, 429), (768, 633), (943, 556)]
refuel_button = (1457,874)
samples_start = (1260,931)
samples_buttons = [(730, 845), (843, 845), (957, 845), (1072, 845), (1180, 845)]
samples_tubes = [(730, 577), (843, 577), (957, 577), (1072, 577), (1180, 577)]
engine_center = (1238, 537)
wires_left = [(562, 269), (562, 459), (562, 641), (562, 832)]
wires_right = [(1338, 269), (1338, 459), (1338, 641), (1338, 832)]
electrical_buttons = [(1226,312), (1226, 574), (1226, 834)]
electrical_bars = [(1226,230), (1226, 495), (1226, 768)]
fuse = (965,542)
task_counter = 0

def menu():
    print("what task would you like to do?")
    print("[0] Troubleshoot")
    print("[1] Start Task")
    print("[2] Card Swipe")
    print("[3] Empty Garbage")
    print("[4] Download")
    print("[5] Navigation")
    print("[6] Shields")
    print("[7] Refuel")
    print("[8] Samples")
    print("[9] Align Engine")
    print("[10] Wires")
    print("[11] Weapons")
    print("[12] Leaves")
    print("[13] Electrical Sliders")
    print("[14] Electrical Circles")
    print("[15] Fuse")
    print("[16] Simon Says")
    print("[17] Chart Course")
    print("[18] Unlock Mainfolds")

    option = int(input("options: "))

    if option == 0:
        troubleshoot()
    if option == 1:
        start_task()
    if option == 2:
        card_swipe()
    if option == 3:
        garbage()
    if option == 4:
        download()
    if option == 5:
        navigation()
    if option == 6:
        shields()
    if option == 7:
        refuel()
    if option == 8:
        samples()
    if option == 9:
        align_engine()
    if option == 10:
        wires()
    if option == 11:
        weapons()
    if option == 12:
        leaves()
    if option == 13:
        electrical_slider()
    if option == 14:
        electrical_circles()
    if option == 15:
        electrical_fuse()
    if option == 16:
        simon_says()
    if option == 17:
        nav()
    if option == 18:
        numbers()


    else:
        print("input not supported")

def next_task():
    global task_counter
    res = task_counter
    task_counter += 1
    print("Done task #", task_counter)
    return res

def troubleshoot():
    while not keyboard.is_pressed('q'):
        #print(pyautogui.position())
        temp = pyautogui.position()
        print(temp)

def start_task():
    pyautogui.click(use_button)
    taskType()
    next_task()

def download():
    pyautogui.click(download_button)
    time.sleep(6)

def navigation():
    pyautogui.click(navigation_center)

def refuel():
    pyautogui.moveTo(refuel_button)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

def card_swipe():
    pyautogui.click(id_card_a)
    time.sleep(.4)
    pyautogui.moveTo(id_card_b)
    pyautogui.dragTo(id_card_c, duration=.6)

def garbage():
    pyautogui.moveTo(garbage_up)
    pyautogui.mouseDown()
    pyautogui.moveTo(garbage_down)
    time.sleep(3)
    pyautogui.mouseUp()
    time.sleep(1.5)

def shields():
    tiles = [(790, 429), (768, 633), (950, 348), (943, 556), (924, 715), (1161, 683), (1153, 414)]
    red = (202, 98, 117)
    img = ImageGrab.grab(bbox=(0,0,1980,1080))
    pix = img.load()
    for tile in tiles:
        print(pix[tile])
        if pix[tile][0] in range(200,210) and pix[tile][1] in range(95,105) and pix[tile][2] in range(115,122):
            pyautogui.click(tile)
            time.sleep(0.1)

def samples():
    pyautogui.click(samples_start)
    time.sleep(70)
    red = (249, 136, 137)
    img = ImageGrab.grab(bbox=(0, 0, 1980, 1080))
    pix = img.load()
    for tube in samples_tubes:
        print(pix[tube])
        if pix[tube] == red:
            pyautogui.click(tube[0],(tube[1]+274))
            time.sleep(0.1)

def align_engine():
    img = ImageGrab.grab(bbox=(0, 0, 1980, 1080))
    array = np.array(img)
    # marker = (65, 65, 70)
    marker = (163, 163, 178)
    y, x = np.where(np.all(array==marker, axis=2))
    pyautogui.moveTo(x[0], y[0])
    pyautogui.mouseDown()
    pyautogui.moveTo(engine_center)
    pyautogui.mouseUp()

def wires():
    img = ImageGrab.grab(bbox=(0, 0, 1400, 905))
    pix = img.load()

    for wire in wires_left:
        for wire2 in wires_right:
            if pix[wire] == pix[wire2]:
                pyautogui.moveTo(wire)
                pyautogui.mouseDown()
                pyautogui.moveTo(wire2)
                pyautogui.mouseUp()

def weapons():
    marker = (55, 112, 66)
    t_end = time.time() + 20
    while time.time() < t_end:
        img = ImageGrab.grab(bbox=(0, 0, 1378, 950))
        array = np.array(img)
        y, x = np.where(np.all(array == marker, axis=2))
        if len(x) != 0:
            pyautogui.click(x[0], y[0])

def leaves():
    marker = (200, 149, 66)
    # marker = (201, 149, 66)
    t_end = time.time() + 20
    while time.time() < t_end:
        img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
        array = np.array(img)
        y, x = np.where(np.all(array == marker, axis=2))
        if len(x) != 0:
            pyautogui.moveTo(x[0], y[0])
            pyautogui.mouseDown()
            pyautogui.moveTo(554, 565, duration=1)
            pyautogui.mouseUp()
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')

def electrical_slider():
    marker = (255, 98, 0)
    while not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed(
            's') and not keyboard.is_pressed('d'):
        img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
        array = np.array(img)
        y, x = np.where(np.all(array == marker, axis=2))
        if len(x) != 0:
            pyautogui.moveTo(x[0], y[0])
            pyautogui.mouseDown()
            pyautogui.moveTo(x[0], (y[0]-100))
            pyautogui.mouseUp()

def electrical_fuse():
    pyautogui.click(fuse)

def electrical_circles():
    marker = (0, 0, 0)
    img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
    pix = img.load()
    while True:
        img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
        pix = img.load()
        if pix[1233, 230] != marker:
            pyautogui.click(1226, 312)
            break
    while True:
        img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
        pix = img.load()
        if pix[1233, 495] != marker:
            pyautogui.click(1226, 574)
            break
    while True:
        img = ImageGrab.grab(bbox=(0, 0, 1409, 985))
        pix = img.load()
        if pix[1233, 768] != marker:
            pyautogui.click(1226, 834)
            break

def simon_says():
    order = []
    lights = [(542, 466), (648, 466), (768, 466), (542, 587), (648, 587), (768, 587), (542, 718), (648, 718), (768, 718)]
    button = [(1134, 466), (1253, 466), (1386, 466), (1134, 587), (1253, 587), (1386, 587), (1134, 718), (1253, 718), (1386, 718)]
    time.sleep(1)
    color = (68, 168, 255)
    img = ImageGrab.grab(bbox=(0, 0, 841, 782))
    pix = img.load()
    for i in range(5):
        flashed = []
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 841, 782))
            pix = img.load()
            for j in range(9):
                if(pix[lights[j]] == color):
                    flashed.append(j)
                    time.sleep(0.3)
            if len(flashed) == (i+1):
                break
        time.sleep(.5)
        print(flashed)
        for k in flashed:
            pyautogui.click(button[k])
            time.sleep(0.2)

def nav():
    color = (36, 111, 160)
    ship = (136, 162, 177)

    screen = [542, 274, 589, 751]
    img = ImageGrab.grab(bbox=screen)
    array = np.array(img)
    y, x = np.where(np.all(array == ship, axis=2))
    if len(x) != 0:
        pyautogui.moveTo(x[0] + screen[0], y[0] + screen[1])
        pyautogui.mouseDown()

    time.sleep(.1)



    screena = [739, 274, 789, 751]
    img = ImageGrab.grab(bbox=screena)
    array = np.array(img)
    y, x = np.where(np.all(array == color, axis=2))
    if len(x) != 0:
        pyautogui.moveTo(x[0]+screena[0], y[0]+screena[1], duration=.3)

    time.sleep(.1)

    screenb = [938, 274, 980, 751]
    img = ImageGrab.grab(bbox=screenb)
    array = np.array(img)
    y, x = np.where(np.all(array == color, axis=2))
    if len(x) != 0:
        pyautogui.moveTo(x[2] + screenb[0], y[3] + screenb[1], duration=.3)

    time.sleep(.1)

    screenc = [1135, 274, 1176, 751]
    img = ImageGrab.grab(bbox=screenc)
    array = np.array(img)
    y, x = np.where(np.all(array == color, axis=2))
    if len(x) != 0:
        pyautogui.moveTo(x[0] + screenc[0], y[0] + screenc[1], duration=.3)

    time.sleep(.1)

    screend = [1338, 274, 1372, 751]
    img = ImageGrab.grab(bbox=screend)
    array = np.array(img)
    y, x = np.where(np.all(array == color, axis=2))
    if len(x) != 0:
        pyautogui.moveTo(x[0] + screend[0], y[0] + screend[1], duration=.3)

    time.sleep(.5)
    pyautogui.mouseUp()

def numbers():
    x=.8
    time.sleep(.2)
    if pyautogui.locateOnScreen('1.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('1.png', confidence=x))
        #print("I can see 1")
    else:
        print("I can't see 1")
    if pyautogui.locateOnScreen('2.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('2.png', confidence=x))
        #print("I can see 2")
    else:
        print("I can't see 2")
    if pyautogui.locateOnScreen('3.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('3.png', confidence=x))
        #print("I can see 3")
    else:
        print("I can't see 3")
    if pyautogui.locateOnScreen('4.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('4.png', confidence=x))
        #print("I can see 4")
    else:
        print("I can't see 4")
    if pyautogui.locateOnScreen('5.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('5.png', confidence=x))
        #print("I can see 5")
    else:
        print("I can't see 5")
    if pyautogui.locateOnScreen('6.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('6.png', confidence=x))
        #print("I can see 6")
    else:
        print("I can't see 6")
    if pyautogui.locateOnScreen('7.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('7.png', confidence=x))
        #print("I can see 7")
    else:
        print("I can't see 7")
    if pyautogui.locateOnScreen('8.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('8.png', confidence=x))
        #print("I can see 8")
    else:
        print("I can't see 8")
    if pyautogui.locateOnScreen('9.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('9.png', confidence=x))
        #print("I can see 9")
    else:
        print("I can't see 9")
    if pyautogui.locateOnScreen('10.png', confidence=x) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('10.png', confidence=x))
        #print("I can see 10")
    else:
        print("I can't see 10")

def taskType():
    for i in range(2):
        if pyautogui.locateOnScreen("download.png", confidence=.9) != None:
            print("running download")
            download()
        if pyautogui.locateOnScreen("upload.png", confidence=.9) != None:
            print("running download")
            download()
        if pyautogui.locateOnScreen("trash.png", confidence=.75) != None:
            print("running garbage")
            garbage()
        if pyautogui.locateOnScreen("wires.png", confidence=.8) != None:
            print("running wires")
            wires()
        if pyautogui.locateOnScreen("simon.png", confidence=.8) != None:
            print("running simon_says")
            simon_says()
        if pyautogui.locateOnScreen("align.png", confidence=.9) != None:
            print("running align_engine")
            align_engine()
        if pyautogui.locateOnScreen("1.png", confidence=.85) != None:
            print("running numbers")
            numbers()
        if pyautogui.locateOnScreen("slider.png", confidence=.8) != None:
            print("running electrical_slider")
            electrical_slider()
        if pyautogui.locateOnScreen("el_circles.png", confidence=.8) != None:
            print("running electrical_circles")
            electrical_circles()
        if pyautogui.locateOnScreen("fuel.png", confidence=.8) != None:
            print("running refuel")
            refuel()
        if pyautogui.locateOnScreen("card.png", confidence=.8) != None:
            print("running card_swipe")
            card_swipe()
        if pyautogui.locateOnScreen("tubes.png", confidence=.8) != None:
            print("running samples")
            samples()
        if pyautogui.locateOnScreen("shield.png", confidence=.8) != None:
            shields()
            print("running shields")
        if pyautogui.locateOnScreen("fuse.png", confidence=.8) != None:
            print("running electrical_fuse")
            electrical_fuse()
        if pyautogui.locateOnScreen("ship.png", confidence=.8) != None:
            print("running nav")
            nav()
        if pyautogui.locateOnScreen("nav_point.png", confidence=.8) != None:
            print("running navigation")
            navigation()
        if pyautogui.locateOnScreen("leaf_vent.png", confidence=.9) != None:
            print("running leaves")
            leaves()
        if pyautogui.locateOnScreen("weapon_point.png", confidence=.8) != None:
            print("running weapons")
            weapons()

# speed = .7
speed = .8
def press(x, y):
    keyboard.press(x)
    time.sleep(y*speed)
    keyboard.release(x)

def press2(x, y, z):
    keyboard.press(x)
    keyboard.press(y)
    time.sleep((z*speed))
    keyboard.release(x)
    keyboard.release(y)


def homing():
    pyautogui.click(200,200)
    for i in range(3):
        keyboard.press('w')
        time.sleep(2/speed)
        # keyboard.release('w')
        keyboard.press('a')
        time.sleep(2/speed)
        keyboard.release('w')
        keyboard.release('a')
    keyboard.press('w')
    time.sleep(.5/speed)
    keyboard.release('w')

def run_around():
    pyautogui.click(200, 200)
    press('s', .25)
    press('d', 2.65)
    press2('s', 'd', .5)
    isTask()                      #download in cafe
    press2('s', 'd', .5)
    isTask()                      #garbage in cafe
    press('s', .75)
    press('d', 1.6)
    press('w', .4)
    isTask()                      #weapons in weapons
    press2('w', 'd', .4)
    press('w', .35)
    isTask()                      #download in weapons
    press2('s', 'd', 1)
    press('d', .1)
    isTask()                      #fuse in weapons
    press('a', .5)
    press('s', 2.05)
    press('a', 1.6)
    isTask()                      #clean o2 filter
    time.sleep(.2)
    isTask()                      #clean o2 filter
    press2('a', 's', .25)
    isTask()                      #garbage in o2
    press('d', .5)
    press('w', .3)
    press('d', .6)
    isTask()                      #fuse in o2
    press('s', .1)
    press('d', 1.4)
    press('s', .5)
    press('d', 2)
    press('w', 1.25)
    press('a', .5)

    press2('w', 's', .5)
    isTask()                      #fuse in nav    ***CENTERS IN TOP LEFT CORNER***
    press('d', .55)
    isTask()                      #download in nav
    press('d', .2)
    isTask()                      #chart course in nav
    press('a', .3)
    press('s', .6)
    press('d', .3)
    press2('w', 'd', .25)
    isTask()                      # center thing in nav
    press('d', .1)
    press('a', .2)
    press2('a','s', .35)
    press('a', .9)
    press('w', .1)
    isTask()                     #fuse in nav
    press('s', .1)
    press('a', 1.2)
    press('s', .725)
    press('a', .9)
    press('s', 1.6)
    press('d', .4)
    isTask()                    #fuse in shields
    press('a', .45)
    press('s', 1.5)
    press('a', .4)
    press2('w', 'a', 1.5)
    isTask()                      #shields in shields  ***Centers at shields corner***

    press('d', .7)
    press('w', .8)
    press('a', 1.6)
    press('s', 1)
    press('d', .3)
    press2('w', 'd', .5)
    isTask()                      #fuse in communications ***Centers in top right corner***


    press('a', .9)
    isTask()                      #download in communications
    press('d', .35)
    press('w', 1)
    press('a', 1.9)
    press('s', 2)
    press2('s', 'd', 1)
    isTask()                      #garbage in storage   ***Centers in the bottom right corner***

    press('a', .3)
    press2('a', 'w', 1.6)
    isTask()                      #fuel in storage
    press2('a', 'w', 1)
    press('w', .5)
    press2('d', 'w', 1.4)
    isTask()                      #wires in storage
    press2('a', 's', 1.4)
    press('s', 1.2)
    press('a', 2)
    press('w', 1.5)
    press2('w', 'a', 2)           #  ***centers at lights pannel***

    press('d', 1.1)
    press('w', .4)
    press2('w', 'd', 2)
    isTask()                        #circles in electrical
    press('a', 1)
    isTask()                        #wires in electrical
    press('a', .5)
    isTask()                        #sliders in electrical
    press('a', .5)
    isTask()                        #download in electrical
    press2('s', 'd', .5)
    press('d', .75)
    press('s', .75)
    press('a', 1)
    press2('w', 'a', 1)             #  ***centers at lights pannel***

    press2('s', 'd', .3)
    press('s', 1.5)
    press('a', 1.05)
    press('w', 1.2)
    press('a', 1.3)
    press('s', .75)
    press2('s', 'd', 1)             #  ***centers at botoom right corner in lower enging***

    press('a', 2)
    isTask()                          #align lower engine
    press('d', .5)
    press('w', .3)
    press('a', .2)
    isTask()                          #refuel lower engine
    press('d', 1.15)
    press('w', 1.2)
    press('a', 1)
    isTask()                          #fuse in lower engine
    press('d', .3)
    press('w', 1.6)

    press('d', 1.25)
    press('s', .4)
    press2('s', 'a', 1)               #  ***centers at botoom left corner in security***

    press2('d', 'w', .5)
    press('w', 1.05)
    press('d', .5)
    isTask()                            #fuse in security
    press2('a', 's', 1.25)

    press('a', .5)
    press('w', .6)
    isTask()                            #wires in security
    press('s', .3)
    press('a', 2.25)
    isTask()                            #simon says in reactor
    press2('w', 'd', 2.5)               #  ***centers at fuse corner in reactor***

    press('a', .3)
    isTask()                              #fuse in reactor
    press('a', .75)
    press2('a', 'w', .6)
    isTask()                              #numbers in reactor
    press('d', .4)
    press2('s', 'd', 1.5)
    press('d', .9)
    press('w', 2)
    press('a', 1)
    press2('a', 's', 1.5)               #  ***centers at bottom left corner in upper engine***

    press('w', .3)
    isTask()                              #align upper enging
    press('d', .5)
    press('w', .3)
    press('a', .2)
    isTask()                              #refuel upper engine
    press('d', 1.15)
    press('w', 1.2)
    press('a', .9)
    isTask()                              #fuse in upper engine
    press('d', .5)
    press2('d', 's', .5)
    press('s', .4)
    press('d', 2.4)
    press('s', 2.5)
    press2('s', 'a', 1.5)                 #  ***centers at bottom left corner in medBay***

    press2('w', 'd', .3)
    press('d', 1)
    isTask()                                #scan in medBay
    press('a', .8)
    press2('s', 'a', 1.5)
    press2('w', 'd', .5)
    press('d', 1.1)
    isTask()                                #samples in medBay
    press('a', .5)
    press2('a', 'w', .7)
    press('w', 1.75)
    press('d', 1.25)
    press('w', 1)
    press2('w', 'a', 1.5)                   #  ***centers at left corner by wires in cafe***

    press('w', .9)
    isTask()
    press('s', .9)
    press2('s', 'd', 2.7)
    press('s', 2)
    press('d', 1.2)
    press('s', 1)
    press2('s', 'a', 1)                   #  ***centers at bottom left corner in admin***

    press2('w', 'd', .1)
    press('d', 1)



def isTask():
    # print("task")
    # time.sleep(.5)
    if pyautogui.locateOnScreen("Task.png", confidence=.95) != None:
        start_task()



def getColor():
    # print(pyautogui.pixel(768, 466))[0]
    print("test")

# homing()
while not keyboard.is_pressed('q'):
        # run_around()
        # break
        taskType()