import time as t
import pyautogui as p

def button():

    # Locate the off button and move to it
    offlist = p.locateCenterOnScreen("ButtonOff.png")
    offmove = p.moveTo(x = offlist[0], y = offlist[1], duration = 0.2)
    print("Moved to the button!")

    # Now we start clicking on the On button with a constant loop until
    # we can upgrade
    print("CLICKING BUTTON!!!")
    while True:
        onbuttonclick = p.click(x=offlist[0], y=offlist[1], clicks=10, interval=0.05, button='left')

    return onbuttonclick

def upgrades1():
    pass
    up1list = p.locateCenterOnScreen("Upgrades1.png")
    up1move = p.moveTo(x = up1list[0], y = up1list[1], duration = 0.2)
    print("Moved to the Upgrades!")

    up1click = p.click(x=up1list[0], y=up1list[1], clicks=5, interval=0.05, button='left')
    print("UPGRADE 1")

    return up1click
    
def upgrades2():
    pass
    up2list = p.locateCenterOnScreen("Upgrades2.png")
    up2move = p.moveTo(x = up2list[0], y = up2list[1], duration = 0.2)
    print("Moved to the Upgrades!")

    up2click = p.click(x=up2list[0], y=up2list[1], clicks=1, interval=0.13, button='left')
    print("UPGRADE 2")

    return up2click

def return1():
    pass

def main():
    while True:
        
        for i in range(0,1):
            upgrades2()
            t.sleep(1)

        for i in range(0,1)
            upgrades1()
            t.sleep(1)
        button()

button()
